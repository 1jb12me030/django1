
import requests
import json
BASE_URL='http://127.0.0.1:8000/'
ENDPOINT='api/'
resp=requests.get('https://pro-api.coinmarketcap.com.')
pdata = resp.json()
#print('Bitcoin price in USD:')
#print(pdata[0]['price_usd'])
print(pdata)
# def get_resource(id=None):
#     data={}
#     if id is not None:
#         data={
#             'id':id
#         }
#     resp=requests.get(BASE_URL+ENDPOINT,data=json.dumps(data))
#     #if resp.status_code in range(200,300):
#     print(resp.status_code)
#     print(resp.json())
# get_resource()   
# def create_resource():
#     new_emp={
#     'eno':700,
#     'ename':'niksss' ,
#     'esal':6000,
#     'eaddr':'sulatanpuri',
#     }
#     resp=requests.get(BASE_URL+ENDPOINT,data=json.dumps(new_emp))
#     print(resp.status_code)
#     print(resp.json())
# create_resource    

    
      
# def get_all():
#     resp=requests.get(BASE_URL+ENDPOINT)
#     print(resp.status_code)
#     print(resp.json())
# def update_resource(id):
    
#     new_emp={
#     'id':id,    
    
    
#     'esal':9999,
#     'eaddr':'laxmi nagar',
#     }
#     resp=requests.put(BASE_URL+ENDPOINT,data=json.dumps(new_emp))
#     print(resp.status_code)
#     print(resp.json())
# update_resource(80)    
# def delete_resource(id):
    
#     #data={}
#     #if id is not None:
#     data={
            
            
#          #  'id':id,
#         }
#     resp=requests.delete(BASE_URL,data=json.dumps(data))
#     print(resp.status_code)
#     print(resp.json())
# delete_resource(50)    
  

   