import psutil
import humanize

def getmemory():
	mem = psutil.virtual_memory()
	print(f"Total: {humanize.naturalsize(mem.total)}")
	print(f"Used: {mem.used}")

if __name__ == "__main__":
	getmemory()
