import requests
import json


res=requests.get('https://api.exchangeratesapi.io/latest?base=USD')
res=res.json()

print(res["rates"])


