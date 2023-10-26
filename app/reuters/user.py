from fastapi import APIRouter
from app.schemas.authentication import UserDetails


router = APIRouter()

@router.post('/user/{user_id}')
def getUser(data: getUser):
    return{"data": data}

@router.put('/user/{user_id}')
def updateUser(data: updateUser):
    return {"data": data}

@router.delete('/user/{user_id}')
def deleteUser(data: deleteUser):
    return {data: deleteUser}
