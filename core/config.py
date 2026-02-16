from motor.asyncio_motor import AsyncIOMotorClient

client = AsyncIOMotorClient("mongodb://121.0.0.1/27017")

db=client["chatbot_db"]