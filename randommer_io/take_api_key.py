import requests 
import json

url='https://randommer.io/api/Card'
h={
    "X-Api-Key":'436a2c69c0de41bd9e4e3d16028b0828'
}

r=requests.get(url=url, headers=h )
r=r.json()

print(r)