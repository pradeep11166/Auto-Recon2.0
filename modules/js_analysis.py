from colorama import Fore
import os

def run(subdomains):
    print(Fore.YELLOW + "Running JavaScript Analysis...")
    for sub in subdomains:
        sub = sub.strip()
        os.system(f"gau {sub} | grep '.js' > output/Js_Analysis/{sub}_js_urls.txt")

