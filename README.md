# Port Scanner

## 📌 Overview
The **Port Scanner** is a Python-based tool that scans a target domain or IP address to identify open ports, detect running services, and provide a security assessment.

## 🚀 Features
- **Scans a range of ports** on a given domain or IP.
- **Retrieves service banners** to determine what is running on open ports.
- **Allows user customization** of the final report, selecting:
  - Domain name
  - IP Address
  - Open Ports & Services
  - Security Notes
- **Multi-threaded scanning** for improved speed.
- **Option to save results** to a text file.
- **Supports stopping the scan** mid-process with `'q'`.

---

## 📥 Installation
### **1️⃣ Install Python**
Ensure Python 3 is installed. Check with:
```sh
python --version
```
If not installed, download it from [python.org](https://www.python.org/downloads/).

### **2️⃣ Install Required Dependencies**
Install the necessary Python libraries:
```sh
pip install colorama
```

---

## ▶️ Running the Script
1. Open a terminal (CMD, PowerShell, or Terminal on Mac/Linux).
2. Navigate to the script's directory:
   ```sh
   cd path/to/port_scanner
   ```
3. Run the script:
   ```sh
   python port_scanner.py
   ```

---

## 📊 Understanding Results
After the scan, a **customizable report** is displayed based on the user's choices. This includes:

- **Domain & IP Address:** Identifies the scanned target.
- **Open Ports & Services:** Lists all detected open ports and their running services.
- **Security Notes:** Warns about potential risks and best practices.

### **Example Output:**
```
🔍 Scanning target.com from port 20 to 80...

[+] Port 22 is OPEN (SSH-2.0-OpenSSH_8.0)
[+] Port 80 is OPEN (Apache HTTPD)

🔎 Domain Report:
Target: target.com
IP Address: 192.168.1.10
Open Ports & Services:
Port 22 is OPEN (SSH-2.0-OpenSSH_8.0)
Port 80 is OPEN (Apache HTTPD)
⚠️ Security Note: Any open ports can be potential security risks. Ensure only necessary ports are open and protected.
```

---

## 💾 Saving Results
After scanning, the user is prompted to **save results** to a file (`port_scan_results.txt`). If declined, results can be discarded automatically.

---

## 🔄 Stopping a Scan
- Press **'q'** at any time to stop an ongoing scan.
- The program ensures that partial results are still available.

---

## 🛠 Future Improvements
- Add **more vulnerability detection** based on the detected services.
- Implement a **GUI version** for easier use.
- Introduce **Nmap integration** for deeper scanning.

---

## 📝 License
This project is open-source and free to use. Contributions are welcome!

