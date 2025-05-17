from fastapi import APIRouter, Depends
from app.auth.dependencies import get_current_user

router = APIRouter(prefix="/secure", tags=["Secure Routes"])

@router.get("/profile")
def read_profile(username: str = Depends(get_current_user)):
    return {"message": f"Welcome, {username}. You are authenticated."}
