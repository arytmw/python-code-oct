from paramiko.client import SSHClient
from paramiko.client import AutoAddPolicy
import sys

def sshone(hostname,user,passwd,cmd):
	client = SSHClient()
	client.set_missing_host_key_policy(AutoAddPolicy)
	client.connect(hostname,username=user,password=passwd)
	stdin, stdout, stderr = client.exec_command(cmd)
	print(stdout.read().decode())
	client.close()

if __name__ == "__main__":
	hostname = sys.argv[1]
	user = sys.argv[2]
	passwd = sys.argv[3]
	cmd = sys.argv[4]
	sshone(hostname,user,passwd,cmd)
