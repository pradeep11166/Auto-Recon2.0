from colorama import Fore
import os

def run(subdomains):
    print(Fore.YELLOW + "Running Parameter Discovery...")
    for sub in subdomains:
        sub = sub.strip()
        os.system(f"python3 tools/ParamSpider/paramspider.py -d {sub} -o output/paramspider/{sub}_params.txt")
