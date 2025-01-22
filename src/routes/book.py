from ..models import Book
from ..database.infra import get_db
from ..database.book import filter_books
from fastapi_crudrouter import SQLAlchemyCRUDRouter
from typing import Annotated, Optional
from fastapi import Query
from datetime import date

book_router = SQLAlchemyCRUDRouter(
    schema=Book,
    db_model=Book,
    db=get_db
)

@book_router.get("")
def get_books(
    id: Optional[int] = None,
    title: Annotated[str | None, Query(min_length=1)] = None,
    publication_date: Optional[date] = None,
    language: Annotated[str | None, Query(min_length=1)] = None,
    authors: Annotated[str | None, Query(min_length=1)] = None,
    genres: Annotated[str | None, Query(min_length=1)] = None
):
    return filter_books(id, title, publication_date, language, authors, genres)