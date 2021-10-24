from urllib import request

import requests
import json

url = 'http://api.stackexchange.com/2.3/questions?key=U4DMV*8nvpm3EOpvf69Rxw((&site=stackoverflow&page=1&pagesize=20&fromdate=1634428800&todate=1634515200&order=desc&sort=votes&filter=default'
headers = {'user-agent': 'my-app/0.0.1'}
response = requests.get(url, headers=headers)
data = json.loads(response.text)

print(data)
