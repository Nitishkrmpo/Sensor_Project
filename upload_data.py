from pymongo.mongo_client import MongoClient
import pandas as pd
import json
uri="mongodb+srv://root:1410@cluster0.k2fcg.mongodb.net/?retryWrites=true&w=majority"
#lets create a new client and connect to server
client=MongoClient(uri)
#create a database and collection name
DATABASE_NAME="Project_Database"
COLLECTION_NAME="waferfault"
df=pd.read_csv("C:\Users\nitis\OneDrive\Desktop\Sensor Project\src\notebooks\wafer_23012020_041211.csv")
df.head()
df=df.drop("Unnamed: 0",axis=1)
df
json_record = list(json.loads(df.T.to_json()).values())
type(json_record)
client[DATABASE_NAME][COLLECTION_NAME].insert_many(json_record)