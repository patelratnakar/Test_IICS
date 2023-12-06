import requests
import json


#Define the Login Call Function
def loginCall(userName, passWord):
    url = "https://dm2-us.informaticacloud.com"
    payload = {
        "username" : "me111089@global.org.in",
        "password" : "Anil1980**"
    }
    payload_json = json.dumps(payload)
    headers = {
            'Accept': 'application/json',
            'Content-Type': 'application/json'
            }
    response = requests.request("POST", url, headers=headers, data = payload_json)
    response_json = response.json() if response and response.status_code == 200 else None
    infa_session_id = response_json['userInfo']['sessionId']
    return infa_session_id
