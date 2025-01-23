from ..models import Sale
from .infra import engine
from sqlmodel import Session, select, func, col
from typing import Optional
from datetime import date


def filter_sales(
    page: int,
    size: int,
    id: Optional[int] = None,
    date: Optional[date] = None,
    payment_type: Optional[str] = None,
    customer_id: Optional[int] = None,
    employee_id: Optional[int] = None,
):
    with Session(engine) as session:
        statement = (
            select(Sale)
            .where(id == None or Sale.id == id)
            .where(date == None or Sale.date == date)
            .where(
                payment_type == None
                or payment_type.lower() in Sale.payment_type.lower()
            )
            .where(customer_id == None or Sale.customer_id == customer_id)
            .where(employee_id == None or Sale.employee_id == employee_id)
        )

        statement = statement.offset((page - 1) * size).limit(size)

        return session.exec(statement).all()


def count():
    with Session(engine) as session:
        statement = select(func.count(col(Sale.id)))

        return session.exec(statement).one()
