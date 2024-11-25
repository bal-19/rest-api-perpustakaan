from motor.motor_asyncio import AsyncIOMotorClient

from core.config import settings


class Database:
    client: AsyncIOMotorClient = None
    
    @classmethod
    async def connect(cls):
        cls.client = AsyncIOMotorClient(settings.MONGO_URL)
    
    @classmethod
    async def close(cls):
        cls.client.close()


db = Database()