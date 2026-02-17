from fastapi import APIRouter
from schemas.Auth_Schema import LoginSchema, RegisterSchema
from services.Auth_Services import Auth_Service
router = APIRouter()

# auth_service=Auth_Service("did@102","divy123")

@router.get("/")
def welcome():
    
    return {"data":"Welcome to Auth page"}

@router.post("/login")
async def login(data:LoginSchema):
    print(":::::::::::::::::::::::::",data)
    auth_service=Auth_Service()
    res=await auth_service.Login(data.email,data.password)
    return {"data":f"User {res} logged in successfully"}

@router.post("/register")
async def register(data:RegisterSchema):
    print(data,":::::::::::::::::::::::::")
    auth_service=Auth_Service()
    res=await auth_service.Register(data.Fullname,data.email,data.password)
    print("Answerrrr",res)
    return {"data":f"User {data.Fullname} registered successfully"}     