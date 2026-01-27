from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def welcome():
    return {"data":"Welcome to Auth page"}
