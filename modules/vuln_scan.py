from colorama import Fore
import os

def run(subdomains):
    print(Fore.YELLOW + "Running Vulnerability Scan with Nuclei...")
    for sub in subdomains:
        sub = sub.strip()
        os.system(f"./tools/nuclei/nuclei -l output/subdomains.txt -t tools/nuclei/nuclei-templates/ -o output/Vuln_scan/{sub}_vulns.txt")

