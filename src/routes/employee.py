from ..models import Employee
from ..database.infra import get_db
from ..database.employee import filter_employees, count, sales_in_time_window
from fastapi_crudrouter import SQLAlchemyCRUDRouter
from typing import Annotated, Optional
from fastapi import Query
from datetime import date

employees_router = SQLAlchemyCRUDRouter(schema=Employee, db_model=Employee, db=get_db)


@employees_router.get("")
def get_employees(
    page: int,
    size: int,
    id: Optional[int] = None,
    first_name: Annotated[str | None, Query(min_length=1)] = None,
    last_name: Annotated[str | None, Query(min_length=1)] = None,
    register_code: Optional[int] = None,
    hired_date: Optional[date] = None,
    wage: Optional[float] = None,
):
    employees = filter_employees(
        page, size, id, first_name, last_name, register_code, hired_date, wage
    )

    return {
        "employees": employees,
        "page": page,
        "size": len(employees),
    }


@employees_router.get("/count/")
def count_books():
    cnt = count()

    return {"count": cnt}


@employees_router.get("/time-window-sales/")
def sales_in_time_window_route(employee_id: int, start_date: date, end_date: date):
    result = sales_in_time_window(employee_id, start_date, end_date)

    return {
        "count": result["count"],
        "value": result["value"],
    }
