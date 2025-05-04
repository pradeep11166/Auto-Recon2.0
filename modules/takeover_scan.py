#from colorama import Fore
#import os
#
#def run(subdomains):
#    print(Fore.YELLOW + "Running Subdomain Takeover Scan...")
#    for sub in subdomains:
#        sub = sub.strip()
#        # Use subzy instead of sub404 for subdomain takeover scan
#        #os.system(f"python3 tools/subzy/subzy.py -d {sub} -o output/{sub}_takeover.txt")
#        os.system(f"./tools/subzy/subzy r --target ./output/subdomain.txt")

from colorama import Fore
import os
import shutil

def run(subdomains, output_dir):
    print(Fore.YELLOW + "Running Subdomain Takeover Scan...")

    # Step 1: Define the subdomains file path dynamically
    subdomains_file = f"{output_dir}/subdomains.txt"
    subzy_file = './tools/subzy/subdomain.txt'

    # Step 2: Copy the subdomains file from output directory to subzy folder
    if os.path.exists(subdomains_file):
        # Ensure the output folder exists and copy the file
        shutil.copy(subdomains_file, subzy_file)
        print(Fore.GREEN + f"Subdomain file copied to subzy folder: {subzy_file}")
    else:
        print(Fore.RED + f"Subdomain file not found at: {subdomains_file}")

    # Step 3: Run subzy with the copied subdomains file
    print(Fore.YELLOW + "Running subzy for subdomain takeover...")
    os.system(f"./tools/subzy/subzy r --targets {subzy_file}")
    print(Fore.GREEN + "Subdomain takeover scan completed. Results saved in output/takeover_results.txt")

