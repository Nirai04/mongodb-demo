import json
from pymongo.mongo_client import MongoClient

db_url = "mongodb+srv://niraimathi:<niraimathi>@cluster0.y2ixacg.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(db_url)

print(client)