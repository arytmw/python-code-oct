filename = input("Enter the path to file: ")

f = open(filename,"r")

for line in f.readlines():
	print(line.strip())

f.close()
print("==========================")
print("File read and closed successfully")
