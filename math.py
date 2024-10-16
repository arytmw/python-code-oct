n1 = int(input("Enter number 1: "))
n2 = int(input("Enter number 2: "))

choice = input("Do you want to add or multiply? (a,m) ")

def add_together(n1,n2):
	print(n1+n2)

def multi_together(n1,n2):
	print(n1*n2)

def main():
	if choice == "a":
		add_together(n1,n2)
	else:
		multi_together(n1,n2)

if __name__ == "__main__":
	main()
