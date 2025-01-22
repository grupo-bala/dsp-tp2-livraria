from ..models import Edition
from ..database.infra import get_db
from ..database.edition import filter_editions
from fastapi_crudrouter import SQLAlchemyCRUDRouter
from typing import Annotated, Optional
from fastapi import Query

edition_router = SQLAlchemyCRUDRouter(
    schema=Edition,
    db_model=Edition,
    create_schema=Edition,
    db=get_db
)

@edition_router.get("")
def get_edtions(
    page: int,
    size: int,
    isbn: Annotated[str | None, Query(min_length=1)] = None,
    price: Optional[float] = None,
    publisher: Annotated[str | None, Query(min_length=1)] = None,
    language: Annotated[str | None, Query(min_length=1)] = None,
    publication_year: Optional[int] = None,
    stock: Optional[int] = None,
    book_id: Optional[int] = None,
):
    editions = filter_editions(page, size, isbn, price, publisher, language, publication_year, stock, book_id)

    return {
        "editions": editions,
        "page": page,
        "size": len(editions)
    }