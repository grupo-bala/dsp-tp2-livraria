from ..models import Book
from ..database.infra import get_db
from ..database.book import filter_books, count
from fastapi_crudrouter import SQLAlchemyCRUDRouter
from typing import Annotated, Optional
from fastapi import Query
from datetime import date

book_router = SQLAlchemyCRUDRouter(schema=Book, db_model=Book, db=get_db)


@book_router.get("")
def get_books(
    page: int,
    size: int,
    id: Optional[int] = None,
    title: Annotated[str | None, Query(min_length=1)] = None,
    publication_date: Optional[date] = None,
    language: Annotated[str | None, Query(min_length=1)] = None,
    author: Annotated[str | None, Query(min_length=1)] = None,
    genre: Annotated[str | None, Query(min_length=1)] = None,
):
    books = filter_books(
        page, size, id, title, publication_date, language, author, genre
    )

    return {
        "books": books,
        "page": page,
        "size": len(books),
    }


@book_router.get("/count/")
def count_books():
    cnt = count()

    return {"count": cnt}
