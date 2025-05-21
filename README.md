# 🔍 AutoRecon 2.0

**AutoRecon 2.0** is a modular, automated web reconnaissance and vulnerability scanning tool with an intuitive **web-based GUI**. Designed for penetration testers and bug bounty hunters, it integrates multiple open-source tools to automate subdomain enumeration, JavaScript analysis, vulnerability detection, and more.

---

## 🚀 Features

- ✅ Web-based GUI with module toggle and scan mode selection
- ✅ Modular architecture for easy customization
- ✅ Integrated tools for recon, scanning, and analysis
- ✅ Logs displayed in real-time with auto-refresh
- ✅ Full scan, recon-only, or vulnerability-only modes
- ✅ Dockerized for easy deployment (coming in AutoRecon 3.0)

---

## 🧩 Modules Integrated

| Module                 | Description                                              |
|------------------------|----------------------------------------------------------|
| Subdomain Enumeration  | Uses `amass`, `assetfinder`, `subfinder` for discovery   |
| Live Host Detection    | Uses `httpx` to identify live subdomains                 |
| Port Scan              | Uses `rustscan` for fast port scanning                   |
| Web Crawler            | Uses `hakrawler` or custom scripts to crawl URLs         |
| Parameter Discovery    | Uses `ParamSpider` to extract GET/POST parameters        |
| JS Analysis            | Uses `LinkFinder` and regex to find secrets/keys         |
| Takeover Scan          | Uses `subzy` or `sub404` for subdomain takeover detection|
| Vulnerability Scan     | Uses `nuclei` for template-based vulnerability scanning  |

---

## 🌐 Web GUI

A simple and responsive web interface built with **Flask** + **Bootstrap** to:

- Enter target domain
- Select scan mode (Recon / Vuln / Full)
- Toggle optional modules
- View real-time scan logs (auto-refresh every 5 seconds)

---

## 📦 Directory Structure

AutoRecon2.0/
├── modules/
│ ├── subdomain_enum.py
│ ├── live_host_detect.py
│ ├── port_scan.py
│ ├── web_crawler.py
│ ├── parameter_discovery.py
│ ├── js_analysis.py
│ ├── vuln_scan.py
│ └── takeover_scan.py
├── static/
│ └── styles.css
├── templates/
│ ├── index.html # Web GUI
│ └── status.html # Scan output log view
├── output/
│ └── [target]/ # All module results stored here
├── autorecon.py # Main web server & controller
├── requirements.txt # Python dependencies
└── README.md # This file


### 🔗 Dependencies

Ensure the following tools are installed and in your `$PATH`:

- `python3`
- `pip3`
- `nmap`
- `subfinder`
- `assetfinder`
- `amass`
- `httpx`
- `nuclei`
- `rustscan`
- `gau`
- `waybackurls`
- `getJS`
- `jsbeautifier`

--- 

### 📦 Python Packages

Install Flask and required modules:

```bash
pip3 install flask colorama pyfiglet

---

## 🛠️ Installation

### 1. 📥 Clone the Repository

```bash
git clone https://github.com/pradeep11166/AutoRecon.git
cd AutoRecon
pip install -r requirements.txt

```

## 🛠️ Required Tools

Ensure the following tools are installed and available in your PATH:

    amass

    subfinder

    assetfinder

    httpx

    rustscan

    nuclei

    paramspider

    linkfinder

    gau

    hakrawler

    subzy or sub404

    openredirex

    gowitness

    blc (broken-link-checker)

    crlfuzz

---

## Launch AutoRecon Web GUI

python3 autorecon.py  # for cli 

python3 app.py  # for gui

Open your browser and go to: http://localhost:5000
2. Use the Web Interface

    Enter your target domain

    Select scan mode:

        Recon Only: Focuses on recon modules

        Vulnerability Only: Focuses on vuln modules

        Full Scan: Runs all modules

    Optionally, select individual modules

    Click Start Scan

    Scan log will auto-update every 5 seconds


## Scan Modes Explained

Mode	Modules Included
Recon   Only	Subdomain Enum, Live Host, Web Crawler, JS  Analysis, Params
Vuln    Only	Takeover Scan, Port Scan, Vuln Scan
Full    Scan	All modules


##Output

All results are saved under the output/<domain>/ directory, organized by module. Logs are printed in the web GUI and also saved for later review



##Security Notes

    Runs OS commands; do not use on unauthorized targets.

    Results are stored locally and not shared.

    In production or shared environments, add authentication and sandboxing.



💡 ## Coming in AutoRecon 3.0

    🐳 Docker support with preinstalled tools

    ☁️ Cloud deployment with persistent DB storage

    🧠 AI/ML-based vulnerability classification

    🗃️ Result database with search and filters

    🧩 Plugin architecture for adding modules easily

    📊 Scan reporting and PDF exports




🙋‍♂️ #Contributing

Pull requests are welcome!

    Fork the project

    Create your feature branch (git checkout -b feature-name)

    Commit your changes (git commit -m 'Add feature')

    Push to the branch (git push origin feature-name)

    Open a pull request



✍️ Author

Pradip Dev
Cybersecurity Enthusiast | Security Researcher | Full Stack Developer
🌐 Website: HackwithPro
🔗 GitHub: @pradeep11166
