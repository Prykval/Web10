from pymongo import MongoClient

def get_mongodb():
    client = MongoClient("mongodb://localhost")

    db = client.web_hm10
    return db