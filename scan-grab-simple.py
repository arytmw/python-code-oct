import socket

def scan_port(ip, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.5)
        result = sock.connect_ex((ip, port))
        if result == 0:
            try:
                banner = sock.recv(1024).decode().strip()
                print(f"Port {port} is open")
                if banner:
                    print(f"Banner: {banner}")
            except:
                print(f"Port {port} is open (No banner)")
        sock.close()
    except:
        pass

def main():
    target = input("Enter the IP address to scan: ")
    start_port = int(input("Enter the starting port number: "))
    end_port = int(input("Enter the ending port number: "))

    print(f"Scanning {target} from port {start_port} to {end_port}")
    
    for port in range(start_port, end_port + 1):
        scan_port(target, port)

    print("Scan complete")

if __name__ == "__main__":
    main()
