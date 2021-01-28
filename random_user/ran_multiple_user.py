import requests
import json

url='https://randomuser.me/api'
param={
    "results":10
}

res=requests.get(url,param)
res=res.json()

result=res["results"]

for i in result:
    print(i["name"])