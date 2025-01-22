from ..models import Book
from ..db import get_db
from fastapi_crudrouter import SQLAlchemyCRUDRouter

book_router = SQLAlchemyCRUDRouter(
    schema=Book,
    db_model=Book,
    db=get_db
)

@book_router.get("")
def get_books():
    return ""