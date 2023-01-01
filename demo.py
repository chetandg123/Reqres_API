import time

import requests

url = "https://reqres.in/api/users?delay=3"

payload={}
headers = {}
start = time.time()
response = requests.request("GET", url, headers=headers, data=payload)
end = time.time()

print('start time: ',start)

print('end time: ',end)

print('Time Delay: ', end - start)