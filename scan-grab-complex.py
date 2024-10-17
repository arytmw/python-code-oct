import socket
import sys
from datetime import datetime

def scan_port(ip, port, timeout=1):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(timeout)
            result = s.connect_ex((ip, port))
            if result == 0:
                try:
                    banner = grab_banner(s)
                    return port, True, banner
                except:
                    return port, True, None
            else:
                return port, False, None
    except:
        return port, False, None

def grab_banner(s):
    return s.recv(1024).decode('utf-8', 'ignore').strip()

def scan_ports(ip, start_port, end_port):
    print(f"Scanning {ip} from port {start_port} to {end_port}")
    start_time = datetime.now()

    open_ports = []
    for port in range(start_port, end_port + 1):
        result = scan_port(ip, port)
        if result[1]:  # If port is open
            open_ports.append(result)
        print(f"Scanning port {port}", end='\r')

    end_time = datetime.now()
    duration = end_time - start_time

    print(f"\nScan completed in {duration}")
    print(f"Open ports: {len(open_ports)}\n")

    for port, _, banner in open_ports:
        print(f"Port {port}: Open")
        if banner:
            print(f"  Banner: {banner}")
        print()

def main():
    if len(sys.argv) != 4:
        print("Usage: python script.py <ip> <start_port> <end_port>")
        sys.exit(1)

    ip = sys.argv[1]
    start_port = int(sys.argv[2])
    end_port = int(sys.argv[3])

    scan_ports(ip, start_port, end_port)

if __name__ == "__main__":
    main()
