import requests
import json

# url='https://randomuser.me/api'

# param={
#     "results":20,
#     "gender":"female"
# }
# res=requests.get(url=url,params=param)

# param={
#     "results":20,
#     "gender":"male"
# }
#  res=requests.get(url=url,params=param)

res=requests.get('https://randomuser.me/api/?results=10&gender=female')

res=res.json()
results=res["results"]

for i in results:
    print(i["name"]["first"],i["location"]["country"])