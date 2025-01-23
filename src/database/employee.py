from ..models import Employee
from .infra import engine
from sqlmodel import Session, select, func, col
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
