import requests

for i in range(10):
    resp = requests.get('http://www.porters.vip/features/rate.html')
    print(resp.status_code)