from src.models import Customer
from .infra import engine
from sqlmodel import Session, select
from typing import Optional

def filter_customers(
    page: int,
    size: int,
    id: Optional[int] = None,
    first_name: Optional[str] = None,
    last_name: Optional[str] = None,
    phone_number: Optional[str] = None,
    email: Optional[str] = None,
    address: Optional[str] = None,
):
    with Session(engine) as session:
        statement = select(Customer) \
            .where(id == None or Customer.id == id) \
            .where(first_name == None or first_name.lower() in Customer.first_name.lower()) \
            .where(last_name == None or last_name.lower() in Customer.last_name.lower()) \
            .where(phone_number == None or phone_number.lower() in Customer.phone_number.lower()) \
            .where(email == None or email.lower() in Customer.email.lower()) \
            .where(address == None or address.lower() in Customer.address.lower())
        
        statement = statement.offset((page - 1) * size).limit(size)
        
        return session.exec(statement).all()