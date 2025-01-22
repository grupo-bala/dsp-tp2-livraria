from datetime import time
import inspect
from fastapi import FastAPI
from fastapi_crudrouter import SQLAlchemyCRUDRouter
from sqlmodel import Session, create_engine
import src.models as models


engine = create_engine("sqlite:///../database.db")
app = FastAPI()

def get_db():
    db = Session(engine)
    try:
        yield db
    finally:
        db.close()

model_classes = [
    obj for name, obj in inspect.getmembers(models, inspect.isclass)
    if obj.__module__ == models.__name__
]

for model in model_classes:
    model_router = SQLAlchemyCRUDRouter(
        schema=model,
        create_schema=model,
        db_model=model,
        db=get_db
    )

    app.include_router(model_router)