import requests
from bs4 import BeautifulSoup

SQL_PAYLOADS = ["' OR '1'='1", "' OR 1=1 --"]
XSS_PAYLOAD = "<script>alert('XSS')</script>"

def scan_sql_injection(url):
    print("\n[+] Scanning for SQL Injection...")
    for payload in SQL_PAYLOADS:
        response = requests.get(url, params={"id": payload})
        if "error" in response.text.lower():
            print(f"[VULNERABLE] SQL Injection detected with payload: {payload}")

def scan_xss(url):
    print("\n[+] Scanning for XSS...")
    response = requests.get(url, params={"search": XSS_PAYLOAD})
    if XSS_PAYLOAD in response.text:
        print("[VULNERABLE] XSS detected!")

def scan_forms(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    forms = soup.find_all("form")
    print(f"[+] Found {len(forms)} forms")

if __name__ == "__main__":
    target = input("Enter target URL: ")
    scan_forms(target)
    scan_sql_injection(target)
    scan_xss(target)
