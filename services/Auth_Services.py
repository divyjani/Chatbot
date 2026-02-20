from core.config import db
from fastapi import HTTPException

class Auth_Service:
    def __init__(self):
        # self.email=email
        # self.password=password
        print("Constructor ")
    async def Login(self, email, password):
        user = await db.users.find_one({"email": email})

        if not user:
            raise HTTPException(status_code=404, detail="User not found")


        if user["password"] != password:
            raise HTTPException(status_code=401, detail="Invalid password")

        return user

    async def Register(self,fullname,email,password):
        existing_user = await db.users.find_one({"email": email})
        if existing_user:
            raise HTTPException(status_code=400, detail="User already exists")

        await db.users.insert_one({
            "fullname": fullname,
            "email": email,
            "password": password
        })

        return {"message": "User registered successfully"}

    def Logout(self):
        print("Logout Functionality has been built successfully")