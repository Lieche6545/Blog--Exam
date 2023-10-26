from fastapi import FastAPI, Depends
from . import schemas, models
from .database import engine
from sqlalchemy import session 

app = FastAPI()


models.Base.metadata.create_all(engine)


@app.post("/blog")
def create(request: schemas.Blog, db: session):
    return db