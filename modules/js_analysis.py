from colorama import Fore
import os

# Banner with ASCII art (fancy)
def print_banner():
    from pyfiglet import Figlet
    from colorama import init, Fore
    init(autoreset=True)
    f = Figlet(font='slant')
    #print(Fore.CYAN + f.renderText('Auto Recon JS Analysis'))
    print(Fore.YELLOW + "   \n    🔥 Auto Recon JS Analysis 🔥\n")


#function for js alalysis. 
def run(subdomains):
    print_banner()
    print(Fore.YELLOW + "Running JavaScript Analysis...")
    for sub in subdomains:
        sub = sub.strip()
        os.system(f"gau {sub} | grep '.js' > output/Js_Analysis/{sub}_js_urls.txt")

