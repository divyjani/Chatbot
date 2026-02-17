from motor.motor_asyncio import AsyncIOMotorClient

client = AsyncIOMotorClient("mongodb://127.0.0.1/27017")

db=client["chatbot_db"]