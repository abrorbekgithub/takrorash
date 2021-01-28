import requests
import json
from pprint import pprint

url='https://randomuser.me/api'
param={
    "results":10
}

res=requests.get(url=url,params=param)
res=res.json()
result=res["results"]

# for i in result:
#     pprint(i)
for i in result:
    a=f'{i["name"]["first"]}   {i["name"]["last"]}   {i["gender"]}   {i["location"]["country"]}    {i["dob"]["age"]}   {i["nat"]}    {i["phone"]} '
    print(a)