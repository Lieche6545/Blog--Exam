from fastapi import APIRouter
from app.schemas.authentication import SignUp
from app.schemas.authentication import LogIn




router = APIRouter()

@router.post('/', status_code=201)
def sign_up(data: SignUp):
    return {"data": data }

@router.post('/', status_code=201)
def login(data: LogIn):
    return {"data": data}