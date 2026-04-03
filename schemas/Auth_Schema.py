from pydantic import BaseModel, EmailStr

class LoginSchema(BaseModel):
    email: EmailStr
    password: str
    # role:str
    
class RegisterSchema(LoginSchema):
    Fullname:str 
    
class TokenSchema(BaseModel):
    token:str

class AdminSchema(BaseModel):
