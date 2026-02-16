from fastapi import APIRouter
from schemas.Auth_Schema import LoginSchema, RegisterSchema
from services.Auth_Services import Auth_Service
router = APIRouter()

Auth_Service("did@102","divy123")

@router.get("/")
def welcome():
    
    return {"data":"Welcome to Auth page"}

@router.post("/login")
def login(data:LoginSchema):
    return {"data":f"User {data.email} logged in successfully"}

@router.post("/register")
def register(data:RegisterSchema):
    ans=Auth_Service.Register(data.Fullname)
    print("Answerrrr",ans)
    return {"data":f"User {data.Fullname} registered successfully"}     