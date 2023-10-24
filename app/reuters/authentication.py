from fastapi import APIRouter
from app.schemas.authentication import SignUp


router = APIRouter

@router.post('/', status_code=201)
def sign_up(data: SignUp):
    return {"data": data }