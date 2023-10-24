from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel
import uvicorn
from app.reuters import authentication

app = FastAPI()
app.include_router(authentication.router, tags= ["authentication"])

@app.get("/")
def home():
    return {"data": "blog list"}

@app.get("/blog/{id}")
def show(id: int):
    #fetch blog with id = id
    return {"data": id}

@app.get("/blog/{id}/comments")
def comments(id):
    return {"data": {"1", "2"}}


class Blog(BaseModel):
    title: str
    body: str
    published: Optional[bool]



@app.post("/blog")
def Create_blog():
    return {"data": "Blog is created"}

if __name__ == "__main__":
    uvicorn.run(app="main:app", reload=True)