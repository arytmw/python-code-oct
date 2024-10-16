import re

raw_file = input("Enter the file containing raw IP data: ")

f = open(raw_file,"r")
ipdata = f.read()
f.close()

result = re.findall(r"\d+\.\d+\.\d+\.\d+",ipdata)

for item in result:
	print(item)

redirect_choice = input("Do you want to redirect the output? (y/n) ")

if redirect_choice.lower()[0] == "y":
	resultfile = input("Enter new file to create: ")
	f = open(resultfile,"w")
	for item in result:
		f.write(item+"\n")
	f.close()
	print(f"IPs extracted into ----> {resultfile}")
elif redirect_choice.lower()[0] == "n":
	pass
else:
	print("Something went wrong!!!")
