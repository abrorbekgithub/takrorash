import requests
import json

# url='https://randomuser.me/api'
# params={
#     "results":15,
#     "nat":'US,GB,AU',
#     "gender":"female"
# }

# res=requests.get(url=url,params=params)

res=requests.get('https://randomuser.me/api/?results=15&nat=US,GB,AU&gender=female')

res=res.json()

results=res["results"]

for i in results:
    print(i["name"]["first"],i["nat"],i["dob"]["age"])