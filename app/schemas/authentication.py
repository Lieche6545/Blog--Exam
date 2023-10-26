from pydantic import BaseModel

class SignUp(BaseModel):
    name: str
    email: str
    password: str

class LogIn(BaseModel):
    username: str
    password: str    

class UserDetails(BaseModel):
    id: str
    name: str
    email: str
    password: str
    