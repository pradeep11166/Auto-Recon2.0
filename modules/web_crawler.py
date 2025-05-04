from colorama import Fore
import os

def run(subdomains):
    print(Fore.YELLOW + "Running Web Crawler...")
    for sub in subdomains:
        sub = sub.strip()
        # Using `gau` to get all URLs from subdomain
        os.system(f"gau {sub} | sort -u | uniq > output/Web_crawl/{sub}_urls.txt")

