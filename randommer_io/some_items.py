
import requests
import json

url='https://randommer.io/api/Card'
h={
    "X-Api-Key":"2b41205aaa7d43a2a036f0f7a558afd6"
}

r=requests.get(url=url,headers=h)
r=r.json()

print(r["type"])