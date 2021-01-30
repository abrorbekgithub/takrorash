import requests
import json

h={"X-Api-Key":'b2b04fed20ce4f0aa33c446c7f606def'}
url='https://randommer.io/api/Card'
p={
    "type":"Visa"
}
r=requests.get( url=url,params=p,headers= h)
r=r.json()
print(r["cvv"])

















# b2b04fed20ce4f0aa33c446c7f606def
