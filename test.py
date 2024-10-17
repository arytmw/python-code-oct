import pexpect

host = "172.31.14.109"
username = "aryan"
password = "networknuts"

def interact():
	ssh_command = f"ssh {username}@{host}"
	child = pexpect.spawn(ssh_command)
	child.expect('password:')
	child.sendline(password)
	child.expect('$')
	child.sendline('touch /tmp/python.txt')
	child.sendline('exit')
	child.expect(pexpect.EOF)

if __name__ == "__main__":
	interact()
