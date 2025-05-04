import os
import subprocess
import platform
from concurrent.futures import ThreadPoolExecutor

# Function to check if host is live
def check_host(host):
    """
    Resolve DNS with nslookup and then ping the host to check if it's live.
    """
    # Try to resolve the host with nslookup
    try:
        result = subprocess.run(['nslookup', host], capture_output=True, text=True)
        if result.returncode != 0 or "Non-existent domain" in result.stdout:
            print(f"[!] DNS resolution failed for {host}")
            return False
    except Exception as e:
        print(f"Error resolving {host} with nslookup: {e}")
        return False

    # Determine platform-specific ping command
    system_platform = platform.system().lower()
    ping_cmd = "ping"
    
    # If on Linux or Unix-based OS, ensure ping is available
    if system_platform in ['linux', 'darwin']:
        if not os.path.exists('/bin/ping') and not os.path.exists('/usr/bin/ping'):
            print("[!] Ping command not found. Please check if ping is installed.")
            return False

        cmd = f"ping -c 1 {host}"
    
    # If on Windows
    elif system_platform == 'windows':
        cmd = f"ping -n 1 {host}"
    else:
        print(f"[!] Unsupported platform: {system_platform}")
        return False

    # Use ping to check if the host is live
    try:
        response = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, check=True, shell=True)
        if "unreachable" in response.stdout.lower():
            print(f"[-] Host {host} is down")
            return False
        return True
    except subprocess.CalledProcessError:
        print(f"[-] Host {host} is down")
        return False
    except Exception as e:
        print(f"Unexpected error while checking host {host}: {e}")
        return False


# Function to scan live hosts in a list of IPs or domains
def scan_live_hosts(hosts):
    """
    Scans a list of hosts to check which ones are live.
    """
    live_hosts = []
    with ThreadPoolExecutor(max_workers=10) as executor:
        results = executor.map(check_host, hosts)

    for host, result in zip(hosts, results):
        if result:
            live_hosts.append(host)
            print(f"[+] Host {host} is live")
        else:
            print(f"[-] Host {host} is down")
    
    return live_hosts


# Function to save only live subdomains back into the same file
def save_live_subdomains(subdomains_file="output/subdomains.txt"):
    """
    Reads subdomains from a file, checks which ones are live using concurrency, 
    and overwrites the file with only live subdomains.
    """
    # Read subdomains
    try:
        with open(subdomains_file, "r") as file:
            subdomains = [line.strip() for line in file.readlines() if line.strip()]
        print(f"[+] Read {len(subdomains)} subdomains from {subdomains_file}")
    except FileNotFoundError:
        print(f"[!] Error: The file {subdomains_file} does not exist.")
        return
    except Exception as e:
        print(f"[!] Error reading file {subdomains_file}: {e}")
        return

    print(f"[*] Checking which of the {len(subdomains)} subdomains are live...")

    live_subdomains = scan_live_hosts(subdomains)

    try:
        with open(subdomains_file, "w") as file:
            for live_sub in live_subdomains:
                file.write(live_sub + "\n")
        print(f"[+] Overwritten {subdomains_file} with {len(live_subdomains)} live subdomains.")
    except Exception as e:
        print(f"[!] Error saving live subdomains to {subdomains_file}: {e}")

# Run function to be used in main.py
def run(subdomains):
    """
    This function runs the live host detection for a list of subdomains.
    """
    # Ensure the subdomains are stripped of unwanted whitespace or newlines
    subdomains = [subdomain.strip() for subdomain in subdomains]
    
    print("Running live host detection...")
    live_hosts = scan_live_hosts(subdomains)

    # Print total number of live hosts
    print(f"\nTotal number of live hosts: {len(live_hosts)}")

    return live_hosts

# Example usage (For testing purposes, you can remove or modify this for integration)
if __name__ == "__main__":
    # Save live subdomains using the file paths
    save_live_subdomains("output/subdomains.txt", "output/new_live_subdomain.txt")

