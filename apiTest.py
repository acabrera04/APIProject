import requests
import json
import sqlalchemy as db
import pandas as pd
url = "https://gamerpower.com/api"

r= requests.post(url + "/giveaways")
pc = requests.get(url + "/giveaways?platform=pc")
#print(pc.json()[0])

df = pd.DataFrame.from_dict(pc.json())
engine = db.create_engine('sqlite:///giveaways.db')

df.to_sql('PC_Giveaways', con=engine, if_exists='replace', index=False)
with engine.connect() as connection:
   query_result = connection.execute(db.text("SELECT * FROM PC_Giveaways;")).fetchall()
   print(pd.DataFrame(query_result))
