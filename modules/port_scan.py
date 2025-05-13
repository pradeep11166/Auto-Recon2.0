import os
import subprocess
import time

# Ensure output directory exists
os.makedirs("output", exist_ok=True)

# Banner with ASCII art (fancy)
def print_banner():
    from pyfiglet import Figlet
    from colorama import init, Fore
    init(autoreset=True)
    f = Figlet(font='slant')
    #print(Fore.CYAN + f.renderText('Port Scan'))
    print(Fore.YELLOW + "   \n    🔥 Port Scan  🔥\n")


# Perform port scan on host
def perform_port_scan(host, use_pn=False):
    print_banner()
    print(f"[*] Scanning {host} (use_pn={use_pn})...")
    nmap_cmd = ["nmap", "-Pn", "-p-", "--min-rate", "1000", "-T3", host]
    if use_pn:
        nmap_cmd.insert(1, "-Pn")  # Insert -Pn after "nmap"

    try:
        result = subprocess.run(nmap_cmd, capture_output=True, text=True, check=True, timeout=120)
        return result.stdout
    except subprocess.TimeoutExpired:
        print(f"[-] Timeout while scanning {host}. Skipping...")
        return None
    except subprocess.CalledProcessError as e:
        print(f"[-] Error scanning {host}: {e.stderr}")
        return None

# Parse ports from Nmap output
def parse_ports(nmap_output):
    open_ports = []
    closed_ports = []
    parsing_ports = False

    for line in nmap_output.splitlines():
        if "PORT" in line and "STATE" in line:
            parsing_ports = True
            continue
        if parsing_ports:
            if line.strip() == "":
                break
            parts = line.split()
            if len(parts) >= 2:
                port_info, state = parts[0], parts[1]
                port_number = port_info.split('/')[0]
                if state.lower() in ["open", "filtered", "open|filtered"]:
                    open_ports.append(port_number)
                elif state.lower() == "closed":
                    closed_ports.append(port_number)

    return open_ports, closed_ports

# Read live subdomains from file
def get_live_subdomains(file_path="output/new_live_subdomains.txt"):
    live_subdomains = []
    try:
        with open(file_path, "r") as file:
            live_subdomains = [line.strip() for line in file.readlines() if line.strip()]
        print(f"[+] Found {len(live_subdomains)} live subdomains.")
    except FileNotFoundError:
        print(f"Error: The file {file_path} does not exist.")
    return live_subdomains

# Main function to run port scan
def run(live_hosts):
    output_file = "output/ports_scan_result.txt"

    if not live_hosts:
        print("[-] No live hosts to scan.")
        return

    with open(output_file, "w") as f_out:
        for host in live_hosts:
            time.sleep(0.5)

            scan_result = perform_port_scan(host)
            open_ports, closed_ports = [], []

            if scan_result:
                open_ports, closed_ports = parse_ports(scan_result)

            if not open_ports:
                print(f"[!] No open ports found for {host}, retrying with -Pn...")
                time.sleep(0.5)
                scan_result_pn = perform_port_scan(host, use_pn=True)
                if scan_result_pn:
                    open_ports, closed_ports = parse_ports(scan_result_pn)

            f_out.write(f"\nHost: {host}\n")

            if open_ports:
                f_out.write("Open Ports:\n")
                for port in open_ports:
                    f_out.write(f"  - {port}\n")
            else:
                f_out.write("Open Ports:\n  - None found\n")

            if closed_ports:
                f_out.write("Closed Ports:\n")
                for port in closed_ports:
                    f_out.write(f"  - {port}\n")
            else:
                f_out.write("Closed Ports:\n  - None found\n")

            print(f"[+] Scan completed for {host}")

    print(f"\n[+] All port scan results saved to {output_file}")


# Run the port scanning process
if __name__ == "__main__":
    run()

