import socket
import threading
import time
import re
from colorama import Fore, Style, init

# Initialize colorama for colored terminal output
init(autoreset=True)

# Function to validate and format the domain name
def format_domain(target):
    if not target.startswith("http"):
        target = "https://" + target
    domain_match = re.search(r'https?://([\w.-]+)(?:\.[a-z]{2,})?', target)
    if domain_match:
        return domain_match.group(1)  # Extracts only the domain name
    return target

# Function to scan a single port and attempt to grab the service banner
def scan_port(target, port, save_results, results):
    try:
        ip = socket.gethostbyname(target)  # Resolve domain to IP
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(1)
            result = s.connect_ex((ip, port))
            if result == 0:
                try:
                    s.send(b'\n')
                    banner = s.recv(1024).decode().strip()
                except:
                    banner = "Unknown Service"
                
                print(Fore.GREEN + f"[+] Port {port} is OPEN ({banner})")
                result_line = f"Port {port} is OPEN ({banner})\n"
                results.append(result_line)
            else:
                result_line = ""
    except Exception as e:
        result_line = ""
    
    if save_results and result_line:
        with open("port_scan_results.txt", "a") as f:
            f.write(result_line)

# Function to start scanning a range of ports
def port_scanner(target, start_port, end_port, save_results, stop_event, report_options):
    print(Fore.BLUE + Style.BRIGHT + f"\n🔍 Scanning {target} from port {start_port} to {end_port}...\n")
    results = []
    
    for port in range(start_port, end_port + 1):
        if stop_event.is_set():
            print(Fore.YELLOW + "\n[!] Scan stopped by user.")
            return
        thread = threading.Thread(target=scan_port, args=(target, port, save_results, results))
        thread.start()
        time.sleep(0.02)  # Small delay to prevent overloading the system
    
    print(Fore.CYAN + "\n✅ Scan completed!\n")
    print(Fore.MAGENTA + "🔎 Domain Report:")
    
    if "domain" in report_options:
        print(Fore.MAGENTA + f"Target: {target}")
    if "ip" in report_options:
        print(Fore.MAGENTA + f"IP Address: {socket.gethostbyname(target)}")
    if "ports" in report_options:
        print(Fore.MAGENTA + "Open Ports & Services:")
        for res in results:
            print(Fore.MAGENTA + res.strip())
    if "security" in report_options:
        print(Fore.RED + "⚠️ Security Note: Any open ports can be potential security risks. Ensure only necessary ports are open and protected.")

# Main script
if __name__ == "__main__":
    import threading

    while True:
        print(Fore.BLUE + Style.BRIGHT + "🔎 Enhanced Port Scanner 🔎")
        
        while True:
            target = input("Enter target IP or domain: ").strip()
            target = format_domain(target)
            try:
                socket.gethostbyname(target)  # Test if the domain is valid
                break
            except socket.gaierror:
                print(Fore.RED + "[!] Invalid domain. Please enter a valid domain or IP address.")
        
        while True:
            try:
                start_port = int(input("Enter start port (default 1): ") or 1)
                if start_port < 1 or start_port > 65535:
                    raise ValueError
                break
            except ValueError:
                print(Fore.RED + "[!] Invalid input. Please enter a valid port number between 1 and 65535.")
        
        while True:
            try:
                end_port = int(input("Enter end port (default 1024): ") or 1024)
                if end_port < start_port or end_port > 65535:
                    raise ValueError
                break
            except ValueError:
                print(Fore.RED + "[!] Invalid input. Please enter a valid port number between 1 and 65535.")
        
        print("\nWhich details would you like in the final report?")
        print("1. Domain Name")
        print("2. IP Address")
        print("3. Open Ports & Services")
        print("4. Security Notes")
        print("5. All of the above")
        report_choice = input("Enter the numbers (comma-separated) or '5' for all: ").strip()
        
        report_options = []
        if "5" in report_choice or report_choice == "":
            report_options = ["domain", "ip", "ports", "security"]
        else:
            if "1" in report_choice:
                report_options.append("domain")
            if "2" in report_choice:
                report_options.append("ip")
            if "3" in report_choice:
                report_options.append("ports")
            if "4" in report_choice:
                report_options.append("security")
        
        save_results = input("Would you like to save the results to a file? (yes/no): ").strip().lower() in ["yes", "y"]
        stop_event = threading.Event()
        
        if save_results:
            with open("port_scan_results.txt", "w") as f:
                f.write(f"Port scan results for {target} (ports {start_port}-{end_port}):\n")
                f.write("=" * 50 + "\n")
        
        scan_thread = threading.Thread(target=port_scanner, args=(target, start_port, end_port, save_results, stop_event, report_options))
        scan_thread.start()
        
        while scan_thread.is_alive():
            user_input = input("Press 'q' to stop scanning: ").strip().lower()
            if user_input == 'q':
                stop_event.set()
                break
        
        another_scan = input("Would you like to scan another site? (yes/no): ").strip().lower()
        if another_scan not in ["yes", "y"]:
            break
        
    while True:
        final_save = input("Would you like to save the final scan results? (yes/no): ").strip().lower()
        if final_save in ["yes", "y"]:
            break
        elif final_save in ["no", "n"]:
            import os
            if os.path.exists("port_scan_results.txt"):
                os.remove("port_scan_results.txt")
                print(Fore.YELLOW + "Scan results file deleted.")
            break
        else:
            print(Fore.RED + "[!] Invalid input. Please enter 'yes' or 'no'.")

