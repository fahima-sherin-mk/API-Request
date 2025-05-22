import requests as rq
base_url = 'http://www.boredapi.com/api/activity/'
payload = {'participants': 1}
request = rq.get(base_url, params=payload)
data = request.json()
print('response:', data)