
import requests
import json
import time

# Jenkins configuration
JENKINS_URL = "http://3.110.114.161:8080/"
JOB_NAME = "sample-pipeline"
USERNAME = "aryan"
API_TOKEN = "11981d89506ec6a50de4ae904a312f955f"

def trigger_pipeline():
    # Construct the Jenkins API URL
    url = f"{JENKINS_URL}/job/{JOB_NAME}/build?"
    
    # Send POST request to trigger the build
    response = requests.post(url, auth=(USERNAME, API_TOKEN))
    
    if response.status_code == 201:
        print("Pipeline job triggered successfully")
        return True
    else:
        print(f"Failed to trigger pipeline job. Error: {response.text}")
        return False

def get_build_status(build_number):
    url = f"{JENKINS_URL}/job/{JOB_NAME}/{build_number}/api/json"
    
    response = requests.get(url, auth=(USERNAME, API_TOKEN))
    
    if response.status_code == 200:
        build_info = json.loads(response.text)
        return build_info['result']
    else:
        print(f"Failed to get build status. Status code: {response.status_code}")
        return None

def main():
    if trigger_pipeline():
        print("Waiting for build to start...")
        time.sleep(10)  # Wait for the build to start
        
        # Get the latest build number
        url = f"{JENKINS_URL}/job/{JOB_NAME}/lastBuild/api/json"
        response = requests.get(url, auth=(USERNAME, API_TOKEN))
        
        if response.status_code == 200:
            build_info = json.loads(response.text)
            build_number = build_info['number']
            
            print(f"Build number: {build_number}")
            
            while True:
                status = get_build_status(build_number)
                if status:
                    print(f"Build status: {status}")
                    if status in ['SUCCESS', 'FAILURE', 'ABORTED']:
                        break
                time.sleep(30)  # Check status every 30 seconds
        else:
            print("Failed to get the latest build number")

if __name__ == "__main__":
    main()
