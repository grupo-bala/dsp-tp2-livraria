from ..models import SaleItem
from ..database.infra import get_db
from ..database.sale_item import filter_sale_items, count
from fastapi_crudrouter import SQLAlchemyCRUDRouter
from typing import Annotated, Optional
from fastapi import Query

sale_item_router = SQLAlchemyCRUDRouter(schema=SaleItem, db_model=SaleItem, db=get_db)


@sale_item_router.get("")
def get_sale_items(
    page: int,
    size: int,
    id: Optional[int] = None,
    quantity: Optional[int] = None,
    discount: Optional[float] = None,
    is_gift: Optional[bool] = None,
    notes: Annotated[str | None, Query(min_length=1)] = None,
    sale_id: Optional[int] = None,
    edition_id: Optional[int] = None,
):
    sale_items = filter_sale_items(
        page, size, id, quantity, discount, is_gift, notes, sale_id, edition_id
    )

    return {
        "sale_items": sale_items,
        "page": page,
        "size": size,
    }


@sale_item_router.get("/count/")
def count_books():
    cnt = count()

    return {"count": cnt}
