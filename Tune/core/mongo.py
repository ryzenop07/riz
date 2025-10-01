from motor.motor_asyncio import AsyncIOMotorClient
from Tune.logging import LOGGER
import config

class MongoDB:
    def __init__(self):
        self.client = None
        self.db = None

    async def connect(self):
        try:
            LOGGER(__name__).info("Connecting to your Mongo Database...")
            self.client = AsyncIOMotorClient(config.MONGO_DB_URI)
            self.db = self.client.RyzenMusic
            LOGGER(__name__).info("Connected to your Mongo Database.")
        except Exception as e:
            LOGGER(__name__).error(f"Failed to connect to MongoDB: {e}")

mongodb = MongoDB()