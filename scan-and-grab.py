from scanner import Scanner
from grabber import Grabber

def main():
	ip = input("Enter the IP to port scan and banner grab: ")
	l_port = int(input("Enter the lower port: "))
	u_port = int(input("Enter the upper port: "))
	myscan = Scanner(ip)
	myscan.scan(l_port,u_port)
	print(f"Open Ports: {myscan.open_ports}")
	print(f"Starting Banner Grabbing on open ports")
	for port in myscan.open_ports:
		try:
			grab = Grabber(ip,port)
			print(f"{port} ---> {grab.read()}")
			grab.close()
		except Exception:
			print(f"Error: {port} is not responding!")


if __name__ == "__main__":
	main()
