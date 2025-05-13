from flask import Flask, render_template, request, redirect, url_for
import subprocess
import threading
import os

app = Flask(__name__)

output_log = []


def run_autorecon(domain, mode, selected_modules):
    global output_log
    output_log.clear()

    command = ["python3", "autorecon.py", "-d", domain, "--mode", mode]

    if selected_modules:
        command.extend(["--modules"] + selected_modules)

    # Run in background and capture output only internally
    process = subprocess.Popen(
        command,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        text=True
    )

    for line in process.stdout:
        output_log.append(line)
        # No print(line, end="") => keeps terminal clean


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        domain = request.form.get("domain")
        mode = request.form.get("mode")
        selected_modules = request.form.getlist("modules")

        # Start scan in a background thread
        threading.Thread(target=run_autorecon, args=(domain, mode, selected_modules), daemon=True).start()

        return redirect(url_for("scan_status"))

    return render_template("index.html")


@app.route("/status")
def scan_status():
    return render_template("status.html", output_log=output_log)


if __name__ == "__main__":
    app.run(debug=True, port=5000)
