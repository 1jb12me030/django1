import requests
BASE_URL = 'http://127.0.0.1:8000/'
# Create your tests here.
ENDPOINT = 'apijsoncbv/'
resp = requests.put(BASE_URL+ENDPOINT)
data = resp.json() 
print(data)
print(resp.text)



