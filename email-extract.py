import re
import sys

emailfile = input("Enter file containing raw email data: ")

f = open(emailfile,"r")

emaildata = f.read()

f.close()

result = re.findall(r"[a-zA-Z0-9_]+@[a-zA-Z0-9_]+\.[a-zA-Z0-9]+",emaildata)

for line in result:
	print(line.strip())

redirect_choice = input("Do you want to redirect the output into a file? (yes/no) ")

if redirect_choice.lower()[0] == "y":
	resultfile = input("Enter file to create for result data: ")
	f = open(resultfile,"w")
	for line in result:
		f.write(line+"\n")
	f.close()
	print("Data redirected successfully!")
	print(f"File ----------> {resultfile}")
elif redirect_choice.lower()[0] == "n":
	pass
else:
	print("ERROR: Please rerun with y or n")
	sys.exit(1)
