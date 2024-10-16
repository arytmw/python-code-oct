from paramiko.client import SSHClient
from paramiko.client import AutoAddPolicy
import sys

def ssh_multi(hostname,username,password):
	try:
		client = SSHClient()
		client.set_missing_host_key_policy(AutoAddPolicy)
		client.connect(hostname,username,password)
		print(f"Successfully connected to {hostname}")
		stdin, stdout, stderr = client.exec_command("lsblk")
		print(f"Output: {stdout.read().decode()}")
		client.close()
		print("Connected closed")
	except Exception as e:
		print(f"Error: {e}")

def connect_to_vms(ipfile,username,password):
		f = open(ipfile,"r")
		ipaddresses = f.readlines()
		f.close()
		for ip in ipaddresses:
			new_ip = ip.strip()
			print(f"Attempting connection to: {new_ip}")
			ssh_multi(new_ip,username,password)

if __name__ == "__main__":
	ipfile = sys.argv[1]
	username = sys.argv[2]
	password = sys.argv[3]
	connect_to_vms(ipfile,username,password)
