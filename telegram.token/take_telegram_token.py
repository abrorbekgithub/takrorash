import requests
import json
token='1690220485:AAHXCPppQIBAypOyRADaSmp3UHsH2UfOhM4'
url=f'https://api.telegram.org/bot{token}/getMe'
r=requests.get(url=url)
r=r.json()
print(r)