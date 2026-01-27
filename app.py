from fastapi import FastAPI
from routes.Auth_Route import router as auth_router
app=FastAPI()

app.include_router(auth_router,prefix="/auth")

@app.get("/")
def welcome():
    return {"message": "Welcome to the chat!"}