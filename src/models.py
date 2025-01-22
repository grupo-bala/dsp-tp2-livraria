from datetime import datetime
from typing import List, Optional
from sqlmodel import Relationship, SQLModel, Field

class Book(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    title: str
    publication_date: datetime
    language: str
    authors: str
    genres: str
    

class Edition(SQLModel, table=True):
    isbn: str = Field(default=None, primary_key=True)
    price: float
    publisher: str
    language: str
    publication_year: int
    stock: int

    book: Book = Relationship()


class Customer(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    first_name: str
    last_name: str
    phone_number: str
    email: str
    address: str


class SaleItem(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    edition: Edition = Relationship()
    quantity: int
    discount: float
    notes: Optional[str]
    is_gift: bool


class Sale(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    date: datetime
    items: List[SaleItem] = Relationship()
    customer: Customer = Relationship()
    payment_type: str
    employee: Customer = Relationship()