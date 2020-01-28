from pymongo import MongoClient

import os

class MongoDataBase():
    def __init__ (self):
        pass
    
    def insert_into_database(self, item):
        pass

    def query_item_in_database(self, queryItem):
        pass
    
    def query_entire_database(self):
        pass
    

if (__name__ == "__main__"):
    mongodb_password = os.environ.get("MONGODB_PASS")
    
    client = MongoClient()
    client = MongoClient(f"mongodb+srv://Rumi:{mongodb_password}@rumi-l3snj.mongodb.net/test?retryWrites=true&w=majority")
    db = client["slickdeals"]