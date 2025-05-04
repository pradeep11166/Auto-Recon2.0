import os
import argparse
import time
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), 'modules'))
sys.path.append(os.path.join(os.path.dirname(__file__), 'tools.gowitness'))
from modules import subdomain_enum, live_host_detect, port_scan, web_crawler, js_analysis, parameter_discovery, vuln_scan, takeover_scan
from tools.gowitness import screenshot

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
    parser.add_argument('--modules', nargs='+', help='Specify individual modules to run (overrides mode)', choices=[
        'subdomain_enum', 'live_host_detect', 'port_scan', 'web_crawler',
        'js_analysis', 'parameter_discovery', 'vuln_scan', 'takeover_scan', 'gowitness'
    ])
    return parser.parse_args()

# Main function to execute everything
def run_auto_recon():
    args = parse_arguments()
    print_banner()

    output = 'output'
    if not os.path.isdir('output'):
        os.makedirs('output')

    selected_modules = args.modules

    print("Enumerating subdomains for the domain...")
    subdomains = subdomain_enum.run(args.domain)

    print("Running live host detection and updating subdomains...")
    live_host_detect.run(subdomains)
    live_host_detect.save_live_subdomains("output/subdomains.txt")

    with open("output/subdomains.txt", 'r') as f:
        subdomains = [line.strip() for line in f.readlines()]

    if selected_modules:
        if 'web_crawler' in selected_modules:
            web_crawler.run(subdomains)
        if 'js_analysis' in selected_modules:
            js_analysis.run(subdomains)
        if 'gowitness' in selected_modules:
            screenshot.run('output/subdomains.txt')
        if 'parameter_discovery' in selected_modules:
            parameter_discovery.run(subdomains)
        if 'vuln_scan' in selected_modules:
            vuln_scan.run(subdomains)
        if 'takeover_scan' in selected_modules:
            takeover_scan.run(subdomains, output)
        if 'port_scan' in selected_modules:
            port_scan.run(subdomains)

    else:
        if args.mode == 'recon' or args.mode == 'full':
            web_crawler.run(subdomains)
            js_analysis.run(subdomains)
            screenshot.run('output/subdomains.txt')
            parameter_discovery.run(subdomains)

        if args.mode == 'vuln' or args.mode == 'full':
            vuln_scan.run(subdomains)
            takeover_scan.run(subdomains, output)

if __name__ == '__main__':
    run_auto_recon()
