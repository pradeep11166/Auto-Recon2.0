import subprocess
import shutil
import os

def run(subdomains_file_path):
    # Make sure All_url/ folder exists
    os.makedirs('All_url', exist_ok=True)
    os.makedirs('output/screenshots', exist_ok=True)  # Create screenshots folder

    destination_path = 'All_url/all_urls.txt'

    try:
        # Only copy if source and destination are different
        if not (os.path.exists(destination_path) and os.path.samefile(subdomains_file_path, destination_path)):
            shutil.copy(subdomains_file_path, destination_path)
            print("[+] Copied output/subdomains.txt to All_url/all_urls.txt")
        else:
            print("[!] Source and destination are the same. Skipping copy.")
    except FileNotFoundError:
        print(f"[-] Source file {subdomains_file_path} not found.")
        return
    except Exception as e:
        print(f"[-] Unexpected error during copy: {e}")
        return

    # Now, read all URLs from All_url/all_urls.txt
    try:
        with open(destination_path, 'r') as f:
            urls = [line.strip() for line in f if line.strip()]
    except Exception as e:
        print(f"[-] Error reading {destination_path}: {e}")
        return

    # Screenshot all URLs using gowitness scan single
    for url in urls:
        try:
            subprocess.run([
                "gowitness", "scan", "single",
                "--url", url,
                "--write-db"
            ], check=True)
            print(f"[+] Screenshot taken for: {url}")
        except subprocess.CalledProcessError:
            print(f"[-] gowitness failed for {url}")

