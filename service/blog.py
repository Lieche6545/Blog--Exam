from jose import jwt
from fastapi import HTTPException, status
# from schema.models import User
from database.db import SessionLocal
from typing import Generator

SECRET_KEY = "mysupersecretkey"
ALGORITHM = "HS256"

class default_Codes:
    
    def get_user_from_token(db, token):
        try:
            payload = jwt.decode(token, SECRET_KEY, algorithms =[ALGORITHM])
            username:str = payload.get("sub") 
            if username is None:
                raise HTTPException(
                    status_code=status.HTTP_401_UNAUTHORIZED, 
                    detail="Invalid Email credentials")
        
            user = db.query(user).filter(user.email==username).first()
            if user is None:
                raise HTTPException(
                    status_code=status.HTTP_401_UNAUTHORIZED, 
                    detail="User is not authorized")
        except Exception as e:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED, 
                detail="Unable to verify credentials")
        
        #if successful, return the user as authenticated, for further processing.
        return user

    
    @staticmethod
    def get_db() -> Generator:
        try:
            db = SessionLocal()
            yield db
        finally:
            db.close()
