import requests
import os

def download_repo(repo_url,save_path):
	try:
		print(f"Download repository from {repo_url}")
		result = requests.get(repo_url)
		if result.status_code == 200:
			os.makedirs(os.path.dirname(save_path),exist_ok=True)
			f = open(save_path,"wb")
			f.write(result.content)
			print(f"Repository downloaded successfully to {save_path}")
		else:
			print("Failed to download repo, please check URL.")
	except Exception as e:
		print(f"Error downloading: {e}")


if __name__ == "__main__":
	repo_url = input("Enter repo URL: ")
	save_path = input("Enter save path")
	download_repo(repo_url,save_path)
