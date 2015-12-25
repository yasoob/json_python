from __future__ import print_function
import json
import requests
import sys

if len(sys.argv) < 2:
    print('[Help] Kindly pass in the user_id')
    sys.exit()

if int(sys.argv[-1]) < 100:
    user_id = sys.argv[-1]
else:
    print('[Help] The user_id needs to be less than 101')
    sys.exit()

url = "http://jsonplaceholder.typicode.com/posts/{}".format(user_id)
data = requests.get(url).json()
print('[Title]:  '+data['title'])
print('[Body]:   '+data['body'])
