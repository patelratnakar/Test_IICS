import requests
import os

URL = os.environ['IICS_LOGIN_URL']
USERNAME = os.environ['IICS_USERNAME']
PASSWORD = os.environ['IICS_PASSWORD']

URL = "https://dm2-us.informaticacloud.com"
BODY = {"username": USERNAME, "password": PASSWORD}

r = requests.post(url = URL, json = BODY)

if r.status_code != 200:
    print("Caught exception: " + r.text)

DEV_BODY = BODY = {"username": IICS_USERNAME,"password": IICS_PASSWORD}

u = requests.post(url = URL, json = BODY)

if u.status_code != 200:
    print("Caught exception: " + r.text)

# extracting data in json format
data = r.json()
uat_data = u.json()

# Set session tokens to the environment
env_file = os.getenv('GITHUB_ENV')

with open(env_file, "a") as myfile:
    myfile.write("sessionId=" + data['userInfo']['sessionId'] + "\n")
    myfile.write("uat_sessionId=" + uat_data['userInfo']['sessionId'] + "\n")
