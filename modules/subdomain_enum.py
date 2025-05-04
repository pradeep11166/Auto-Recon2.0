import os
import shutil
from colorama import Fore

def run(domain):
    output_dir = "output"
    
    # Clean and recreate the output directory
    if os.path.isdir(output_dir):
        shutil.rmtree(output_dir)
    os.makedirs(output_dir, exist_ok=True)
    os.makedirs("output/Web_crawl", exist_ok=True)
    os.makedirs("output/All_url", exist_ok=True)
    os.makedirs("output/Js_Analysis", exist_ok=True)
    os.makedirs("output/Vuln_scan", exist_ok=True)
    
    print(Fore.GREEN + "Running Subdomain Enumeration with Subfinder...")

    # Run Subfinder to find subdomains for the domain and store the output in a file
    subfinder_command = f"subfinder -d {domain} -o {output_dir}/subdomains.txt"
    os.system(subfinder_command)

    # Check if subdomains were found
    subdomains_file = f"{output_dir}/subdomains.txt"
    if os.path.exists(subdomains_file) and os.path.getsize(subdomains_file) > 0:
        print(Fore.GREEN + "Subdomains Found:")
        with open(subdomains_file, "r") as file:
            subdomains = file.readlines()
        return subdomains
    else:
        print(Fore.RED + "No subdomains found!")
        return []

def archive_output():
    """Move the output folder to an Archived_Outputs folder with a timestamp."""
    import datetime

    output_dir = "output"
    archive_root = "Archived_Outputs"
    
    if not os.path.isdir(output_dir):
        print(Fore.YELLOW + "No output directory to archive.")
        return

    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    destination_folder = os.path.join(archive_root, f"Run_{timestamp}")

    os.makedirs(destination_folder, exist_ok=True)

    for item in os.listdir(output_dir):
        s = os.path.join(output_dir, item)
        d = os.path.join(destination_folder, item)
        shutil.move(s, d)

    shutil.rmtree(output_dir)
    print(Fore.CYAN + f"Output archived to {destination_folder}")

# Example usage
if __name__ == "__main__":
    domain = input(Fore.BLUE + "Enter the domain to enumerate: ")
    subdomains = run(domain)
    archive_output()

