import requests
import json

url = "https://gamerpower.com/api"

r= requests.post(url + "/giveaways")
pc = requests.get(url + "/giveaways?platform=pc")
print(pc.json()[0])