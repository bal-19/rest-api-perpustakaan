import pymongo
import os

from dotenv import load_dotenv

load_dotenv()
class FetchDataPerpustakaan:
    def __init__(self) -> None:
        self.mongo_url = os.getenv("MONGODB_CONNECTION_STRING")
        self.client = pymongo.MongoClient(self.mongo_url)
        self.db = self.client["perpustakaan"]
        self.collection = self.db["data"]
    
    def get_all(self, page: int, limit: int) -> dict:
        offset = (page - 1) * limit

        result = list(
            self.collection.find()
            .skip(offset)
            .limit(limit)
        )
        
        total_data = self.collection.count_documents({})
        for data in result:
            data.pop("_id")
        
        return {
            "page": page,
            "limit": limit,
            "total_data": total_data,
            "total_pages": (total_data + limit - 1) // limit,
            "result": result
        }
    
    def get_by_search(self, value: str, page: int, limit: int) -> dict:
        filter_mongo = {"nama": {"$regex": value, "$options": "i"}}
        offset = (page - 1) * limit

        result = list(
            self.collection.find(filter_mongo)
            .skip(offset)
            .limit(limit)
        )

        total_data = self.collection.count_documents(filter_mongo)
        for data in result:
            data.pop("_id")
        
        return {
            "query": value,
            "page": page,
            "limit": limit,
            "total_data": total_data,
            "total_pages": (total_data + limit - 1) // limit,
            "result": result
        }
    
    def get_by_filter(self, key: str, value: str, page: int, limit: int) -> dict:
        filter_mongo = {key: value}
        offset = (page - 1) * limit

        result = list(
            self.collection.find(filter_mongo)
            .skip(offset)
            .limit(limit)
        )

        total_data = self.collection.count_documents(filter_mongo)
        for data in result:
            data.pop("_id")
        
        return {
            "column": {
                "key": key,
                "value": value
            },
            "page": page,
            "limit": limit,
            "total_data": total_data,
            "total_pages": (total_data + limit - 1) // limit,
            "result": result
        }