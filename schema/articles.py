from pydantic import BaseModel, EmailStr
from datetime import date


class Blog(BaseModel):
    title: str
    content: str  = 'Be As Creative As You Can Here'

class BlogCreate(Blog):
    pass
class ShowBlog(Blog):
    author: str
    date_posted: date
    class Config:
        orm_mode = True