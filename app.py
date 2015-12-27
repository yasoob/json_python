from __future__ import print_function
import json
import requests
import sys

if len(sys.argv) < 2:
    print('[Help] python app.py <user_id>\n<user_id> should be from between 0 to 100')
    sys.exit()
try:
	user_id = int(sys.argv[-1])
except ValueError as e:
	print("[Error] Please input an integer from 0 to 100")
	sys.exit(-1)

if user_id < 100:
    user_id = sys.argv[-1]
else:
    print('[Help] The user_id needs to be less than 101')
    sys.exit()

url = "http://jsonplaceholder.typicode.com/posts/{}".format(user_id)
try:
	data = requests.get(url).json()
except requests.exceptions.ConnectionError as e:
	print("[Error] There was a network error")
	print(e)
	sys.exit()

print('[Title]:  '+data['title'])
print('[Body]:   '+data['body'])
