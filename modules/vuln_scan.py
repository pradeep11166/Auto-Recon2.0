from colorama import Fore
import os


# Banner with ASCII art (fancy)
def print_banner():
    from pyfiglet import Figlet
    from colorama import init, Fore
    init(autoreset=True)
    f = Figlet(font='slant')
    #print(Fore.CYAN + f.renderText('Vulnerability Scan'))
    print(Fore.YELLOW + "   \n    🔥 Vulnerability Scan 🔥\n")

def run(subdomains):
    print_banner()
    print(Fore.YELLOW + "Running Vulnerability Scan with Nuclei...")
    for sub in subdomains:
        sub = sub.strip()
        os.system(f"./tools/nuclei/nuclei -l output/subdomains.txt -t tools/nuclei/nuclei-templates/ -o output/Vuln_scan/{sub}_vulns.txt")

