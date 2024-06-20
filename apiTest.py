import requests
import json

url = "https://gamerpower.com/api"

r= requests.post(url + "/giveaways")

print(r.json())