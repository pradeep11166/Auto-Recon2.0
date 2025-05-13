from colorama import Fore
import os


# Banner with ASCII art (fancy)
def print_banner():
    from pyfiglet import Figlet
    from colorama import init, Fore
    init(autoreset=True)
    f = Figlet(font='slant')
    #print(Fore.CYAN + f.renderText('Web Crawl'))
    print(Fore.YELLOW + "    \n   🔥 Web Crawl 🔥\n")

def run(subdomains):
    print_banner()
    print(Fore.YELLOW + "Running Web Crawler...")
    for sub in subdomains:
        sub = sub.strip()
        # Using `gau` to get all URLs from subdomain
        os.system(f"gau {sub} | sort -u | uniq > output/Web_crawl/{sub}_urls.txt")

