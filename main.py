from fastapi import FastAPI, Depends
from service.blog import default_Codes
from sqlalchemy.orm import Session
from schema.models import Blogs, User
from database.db import engine, Base
from router.user import user_route
from router.blog import blog_route
from router.admin import admin_route
from router.login import login_route
from schema.articles import ShowBlog
from typing import List



description = """
### OVERVIEW
* Welcome to my blog api. The fundamental concept is that 
anyone visiting the website can be able to read a blog  
post written by them or another user, but would be required to login before they can edit or delete a blog post
*  The Blog application should have
a user authentication where a user can create an account and login so that they could be able to
create a blog, also the Blog should have the logout ability.
* Created in October 2023
"""

contact = {
    'name': 'Victor Amaliechi',
    'Student ID': 'ALT/SOE/022/5457',
    'email': 'noblej.victor@gmail.com',
    'github': 'https://github.com/Lieche6545'
}


tags = [
    {'name': 'Home',
    'description': 'Welcome page route'
    },
    {'name': 'Users',
    'description': 'This are the users related routes'
    },
    {'name': 'Articles',
    'description': 'This are the Articles related routes'
    },
    {'name': 'Admin',
    'description': 'This are the Administrators routes, It was created to help clear my database during testing'
    },
    {'name': 'Login',
    'description': 'Login routes'
    }
]

#read metadata, and instructing it to create tables using base schema.
Base.metadata.create_all(bind=engine)

#FastAPI Matadata.
app = FastAPI(  
    title='Lieche Blog', 
    description = description,
    contact= contact,
    version= '0.0.1',
    openapi_tags= tags
)

app.include_router(user_route, prefix='/user', tags=['Users'])
app.include_router(blog_route, prefix='/article', tags=['Articles'])
app.include_router(admin_route, prefix='/admin', tags=['Admin'])
app.include_router(login_route, prefix='/login', tags=['Login'])


#view aLL articles
@app.get('/view_all', tags=['Home'], response_model= List[ShowBlog])
def get_all_articles(db:Session=Depends(default_Codes.get_db)):
    all_blogs = db.query(Blogs).all()
    return all_blogs
