from ..models import Employee, Sale, SaleItem, Edition
from .infra import engine
from sqlmodel import Session, select, func, col, text
from typing import Optional
from datetime import date


def filter_employees(
    page: int,
    size: int,
    id: Optional[int] = None,
    first_name: Optional[str] = None,
    last_name: Optional[str] = None,
    register_code: Optional[int] = None,
    hired_date: Optional[date] = None,
    wage: Optional[float] = None,
):
    with Session(engine) as session:
        statement = (
            select(Employee)
            .where(id == None or Employee, id == id)
            .where(
                first_name == None or first_name.lower() in Employee.first_name.lower()
            )
            .where(last_name == None or last_name.lower() in Employee.last_name.lower())
            .where(register_code == None or Employee.register_code == register_code)
            .where(hired_date == None or Employee.hired_date == hired_date)
            .where(wage == None or Employee.wage == wage)
        )

        statement = statement.offset((page - 1) * size).limit(size)

        return session.exec(statement).all()


def count():
    with Session(engine) as session:
        statement = select(func.count(col(Employee.id)))

        return session.exec(statement).one()


def sales_in_time_window(employee_id, start_date, end_date):
    with engine.connect() as con:
        result = con.execute(
            text(
                "SELECT sale.id FROM sale WHERE sale.employee_id = :employee_id AND sale.date BETWEEN :start_date AND :end_date"
            ),
            {
                "employee_id": employee_id,
                "start_date": start_date,
                "end_date": end_date,
            },
        ).all()

        sales_ids = [x[0] for x in result]

        if len(sales_ids) == 0:
            return {
                "count": 0,
                "sales": 0,
            }

        result = con.execute(
            text("""
                SELECT IFNULL(SUM(saleitem.quantity * ((100 - saleitem.discount) / 100) * edition.price), 0)
                FROM saleitem
                JOIN edition ON edition.isbn = saleitem.edition_id
                WHERE saleitem.id IN (:ids)
            """),
            {"ids": ", ".join(map(str, sales_ids))},
        ).all()

        return {"value": result[0][0], "count": len(sales_ids)}
