from ..models import Customer
from ..database.infra import get_db
from ..database.customer import filter_customers, count
from fastapi_crudrouter import SQLAlchemyCRUDRouter
from typing import Annotated, Optional
from fastapi import Query

customer_router = SQLAlchemyCRUDRouter(schema=Customer, db_model=Customer, db=get_db)


@customer_router.get("")
def get_customers(
    page: int,
    size: int,
    id: Optional[int] = None,
    first_name: Annotated[str | None, Query(min_length=1)] = None,
    last_name: Annotated[str | None, Query(min_length=1)] = None,
    phone_number: Annotated[str | None, Query(min_length=1)] = None,
    email: Annotated[str | None, Query(min_length=1)] = None,
    address: Annotated[str | None, Query(min_length=1)] = None,
):
    customers = filter_customers(
        page, size, id, first_name, last_name, phone_number, email, address
    )

    return {
        "customers": customers,
        "page": page,
        "size": len(customers),
    }


@customer_router.get("/count/")
def count_books():
    cnt = count()

    return {"count": cnt}
