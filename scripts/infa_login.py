import requests
import os
import json

URL = os.environ['IICS_LOGIN_URL']
USERNAME = os.environ['IICS_USERNAME']
PASSWORD = os.environ['IICS_PASSWORD']

URL = "https://dm2-us.informaticacloud.com"
BODY = {"username": USERNAME, "password": PASSWORD}

r = requests.post(url = URL, json = BODY)

if r.status_code != 200:
   # print("Caught exception: " + r.text)
infa_session_id = response_json['userInfo']['sessionId']
# extracting data in JSON format
#data = r.json()

# Set session tokens to the environment
env_file = os.getenv('GITHUB_ENV')

with open(env_file, "a") as myfile:
    myfile.write("sessionId=" + data['userInfo']['sessionId'] + "\n")
    
