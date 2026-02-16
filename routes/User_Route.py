from fastapi import APIRouter

router=APIRouter()

@router.get("/get_all_users")
def Get_All():
    print("Users Registered successfully")