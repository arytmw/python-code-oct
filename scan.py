from scanner import Scanner

def main():
	ip = input("Enter the IP to scan: ")
	myscan = Scanner(ip)	
	myscan.scan(1,25)
	print(myscan.open_ports)

if __name__ == "__main__":
	main()
