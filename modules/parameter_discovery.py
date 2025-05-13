from colorama import Fore
import os

# Banner with ASCII art (fancy)
def print_banner():
    from pyfiglet import Figlet
    from colorama import init, Fore
    init(autoreset=True)
    f = Figlet(font='slant')
    #print(Fore.CYAN + f.renderText('ParamSpider'))
    print(Fore.YELLOW + "   \n    🔥 paramspider 🔥\n")

 #Function For Paramspider Discovery   
def run(subdomains):
    print_banner()
    print(Fore.YELLOW + "Running Parameter Discovery...")
    for sub in subdomains:
        sub = sub.strip()
        os.system(f"python3 tools/ParamSpider/paramspider.py -d {sub} -o output/paramspider/{sub}_params.txt")
