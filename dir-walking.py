import os
import time

parent_path = input("Enter parent path to search in: ")

def walking(parent_path):
	print(f"Starting directory walk on {parent_path}")
	children = os.listdir(parent_path)
	for child in children:
		child_path = os.path.join(parent_path,child)
		if os.path.isfile(child_path):
			child_info = os.stat(child_path)
			print(f"File Path: {child_path}")
			print(f"\tFile Size: {child_info.st_size} B")
			print(f"\tFile Access Time: {time.ctime(child_info.st_atime)}")
			print(f"\tFile Modified Time: {time.ctime(child_info.st_mtime)}")
			print(f"\tFile Owner UID: {child_info.st_uid}")
			print("==============")
		elif os.path.isdir(child_path):
			walking(child_path)

if __name__ == "__main__":
	walking(parent_path)
