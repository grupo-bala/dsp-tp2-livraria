from ..models import Sale
from ..database.infra import get_db
from ..database.sale import filter_sales, count
from fastapi_crudrouter import SQLAlchemyCRUDRouter
from typing import Annotated, Optional
from fastapi import Query
from datetime import date

sale_router = SQLAlchemyCRUDRouter(schema=Sale, db_model=Sale, db=get_db)


@sale_router.get("")
def get_sales(
    page: int,
    size: int,
    id: Optional[int] = None,
    date: Optional[date] = None,
    payment_type: Annotated[str | None, Query(min_length=1)] = None,
    customer_id: Optional[int] = None,
    employee_id: Optional[int] = None,
):
    sales = filter_sales(page, size, id, date, payment_type, customer_id, employee_id)

    return {
        "sales": sales,
        "page": page,
        "size": len(sales),
    }


@sale_router.get("/count/")
def count_books():
    cnt = count()

    return {"count": cnt}
