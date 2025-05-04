import os
import argparse
import time
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), 'modules'))
sys.path.append(os.path.join(os.path.dirname(__file__), 'tools.gowitness'))
from modules import subdomain_enum, live_host_detect, port_scan, web_crawler, js_analysis, parameter_discovery, vuln_scan, takeover_scan
from tools.gowitness import screenshot
#from modules.port_scan import run

# Banner with ASCII art (fancy)
def print_banner():
    from pyfiglet import Figlet
    from colorama import init, Fore
    init(autoreset=True)
    f = Figlet(font='slant')
    print(Fore.CYAN + f.renderText('Auto Recon'))
    print(Fore.YELLOW + "       🔥 Automated Recon Tool by Pradip 🔥\n")

# Argument parser for input
def parse_arguments():
    parser = argparse.ArgumentParser(description='Auto Recon - A tool for Automated Web Recon and Vulnerability Scanning')
    parser.add_argument('-d', '--domain', help='Domain name to target [e.g., hackerone.com]', required=True)
    parser.add_argument('--subdomain', help='Use Subdomains for scanning [e.g., --subdomain subdomains.txt]', action='store_true')
    parser.add_argument('--mode', help='Choose mode: recon, vuln, full', choices=['recon', 'vuln', 'full'], default='full')
    return parser.parse_args()

# Main function to execute everything
def run_auto_recon():
    # Parse arguments
    args = parse_arguments()
    
    # Banner for UI
    print_banner()

    # Output folders creation
    output = 'output'
    if not os.path.isdir('output'):
        os.makedirs('output')

    # Start subdomain enum if subdomains are not provided
    if args.subdomain:
        print("Using provided subdomains...")
        subdomains = open(args.subdomain, 'r').readlines()
    else:
        print("Enumerating subdomains for the domain...")
        subdomains = subdomain_enum.run(args.domain)

    # Decide mode of operation
    if args.mode == 'recon' or args.mode == 'full':
        # Run all Recon Tasks
        web_crawler.run(subdomains)
        js_analysis.run(subdomains)
        screenshot.run('output/subdomains.txt')
        parameter_discovery.run(subdomains)
    
    if args.mode == 'vuln' or args.mode == 'full':
        # Run Vulnerability Scanning Tasks
        vuln_scan.run(subdomains)
        takeover_scan.run(subdomains, output)
        live_host_detect.run(subdomains)
        live_host_detect.save_live_subdomains("output/subdomains.txt", "output/new_live_subdomain.txt")
        #port_scan.run(subdomains)

if __name__ == '__main__':
    run_auto_recon()

