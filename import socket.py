import socket

def port_scanner(target, ports):
    print("\n[+] Port Scanning Started")
    for port in ports:
        try:
            sock = socket.socket()
            sock.settimeout(1)
            sock.connect((target, port))
            print(f"[OPEN] Port {port}")
            sock.close()
        except:
            pass

def brute_force(username, password_list):
    print("\n[+] Brute Force Simulation")
    for password in password_list:
        print(f"Trying: {password}")
        if password == "admin123":
            print("[SUCCESS] Password Found:", password)
            return
    print("[FAILED] Password not found")

if __name__ == "__main__":
    target_ip = input("Enter target IP: ")
    port_scanner(target_ip, [21, 22, 80, 443])

    brute_force("admin", ["1234", "password", "admin123", "root"])
