import requests
for i in range(10):
    resp = requests.get('http://www.porters.vip:8090/rate.html')
    print(resp.status_code)