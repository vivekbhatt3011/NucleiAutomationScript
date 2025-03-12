# **Nuclei Automation Script**  
![image](https://github.com/user-attachments/assets/8d46d71e-387e-4bd9-b344-9d7db3988021)

This repository contains a **Python automation script** for running [Nuclei](https://github.com/projectdiscovery/nuclei), a fast and customizable vulnerability scanner. The script automates scanning multiple targets using specified templates and saves the results for further analysis.  

## **Features**  
✅ Automates Nuclei scans for bulk targets  
✅ Uses **custom or default templates** for security testing  
✅ Saves results to a file for **better analysis**  
✅ Supports **error handling** for failed executions  

## **Installation**  
Ensure you have **Nuclei** installed before running the script:  
```bash
go install -v github.com/projectdiscovery/nuclei/v2/cmd/nuclei@latest
```
Clone this repository:  
```bash
git clone https://github.com/your-username/nuclei-automation.git
cd nuclei-automation
```

## **Usage**  
Run the script with the required arguments:  
```bash
python nuclei_automation.py -l targets.txt -t ~/nuclei-templates -o results.txt
```
### **Arguments**  
- `-l` / `--list` → **Target file** (List of URLs or IPs)  
- `-t` / `--templates` → **Path to Nuclei templates**  
- `-o` / `--output` (Optional) → **Output file for results** (default: `nuclei_results.txt`)  

## **Example**  
```bash
python nuclei_automation.py -l targets.txt -t ~/nuclei-templates -o scan_results.txt
```

## **License**  
This project is open-source and licensed under **MIT License**.

---

Let me know if you want any modifications! 🚀
