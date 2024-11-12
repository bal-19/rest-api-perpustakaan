import requests
import pymongo
import os

from dotenv import load_dotenv
from bs4 import BeautifulSoup
from fastapi import HTTPException
from datetime import datetime
from typing import List

load_dotenv()
class FetchDataPerpustakaan:
    def __init__(self) -> None:
        self.mongo_url = os.getenv("MONGODB_CONNECTION_STRING")
        self.client = pymongo.MongoClient(self.mongo_url)
        self.db = self.client["perpustakaan"]
        self.collection = self.db["data"]
    
    def get_all(self):
        result = list(self.collection.find())
        for data in result:
            data.pop("_id")
        
        return result
    
    def get_by_search(self, value: str):
        filter_mongo = {"nama": {"$regex": value, "$options": "i"}}
        result = list(self.collection.find(filter_mongo))
        for data in result:
            data.pop("_id")
        
        return result
    
    def get_by_filter(self, key: str, value: str):
        filter_mongo = {key: value}
        result = list(self.collection.find(filter_mongo))
        for data in result:
            data.pop("_id")
        
        return result