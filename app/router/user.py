from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from service.Blog_services import reusables_codes
from schema.user_schema import UserCreate, EditUser, ShowUser
from schema.models import User
from router.login_router import oauth2_scheme


user_route = APIRouter()

@user_route.post('/sign-up', response_model = ShowUser)
async def register_user(new_user: UserCreate, db:Session=Depends(reusables_codes.get_db)):

    emails = db.query(User).all()
    for row in emails:
        if row.email == new_user.email:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED, detail="Email already in use")
        if row.nickname == new_user.nickname:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Nickname already in use, Try another nickname")
    
    new_user = User(
        firstname=new_user.firstname,
        lastname=new_user.lastname,
        nickname= new_user.nickname,
        email = new_user.email,
        password = new_user.password,
    )
    
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    
    return new_user


@user_route.put("/update/{id}")
async def Edit_User_Info(id:int, input:EditUser, db:Session = Depends(reusables_codes.get_db), token:str=Depends(oauth2_scheme)):
    
    
    user = reusables_codes.get_user_from_token(db, token)
    
    existing_user = db.query(User).filter(User.id==id)
    if not existing_user.first():
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail=f"User with:{id} does not exist"
        )
    
    if existing_user.first().id == user.id: 
        existing_user.update(input.__dict__ )                  
        db.commit()
        raise HTTPException(
            status_code=status.HTTP_202_ACCEPTED, 
            detail='Information updated successfully'
        )

    raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, 
            detail= 'User Information can only be EDITED by Owner'
        )

#DELETE MY ACCOUNT Owner ONLY
@user_route.delete("/delete/{id}")
async def Delete_My_account(id:int, db:Session=Depends(reusables_codes.get_db), token:str=Depends(oauth2_scheme)):
    
    
    user = reusables_codes.get_user_from_token(db, token)
    
    existing_user = db.query(User).filter(User.id==id)
    if not existing_user.first():
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail=f"User with:{id} does not exist"
        )
    
    if existing_user.first().id == user.id: 
        existing_user.delete()                  
        db.commit()
        raise HTTPException(
            status_code=status.HTTP_202_ACCEPTED, 
            detail='Account deleted successfully'
        )

    raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, 
            detail= 'Owners permission required'
        )
