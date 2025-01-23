from datetime import datetime
from typing import List, Optional
from sqlmodel import Relationship, SQLModel, Field


class Book(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    title: str
    publication_date: datetime
    language: str
    author: str
    genre: str


class Edition(SQLModel, table=True):
    isbn: str = Field(default=None, primary_key=True)
    price: float
    publisher: str
    language: str
    publication_year: int
    stock: int

    book_id: int = Field(foreign_key="book.id")
    book: Book = Relationship()


class Customer(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    first_name: str
    last_name: str
    phone_number: str
    email: str
    address: str


class Employee(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    first_name: str
    last_name: str
    register_code: int
    hired_date: datetime
    wage: float


class Sale(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    date: datetime
    payment_type: str

    items: List["SaleItem"] = Relationship()

    customer_id: int = Field(foreign_key="customer.id")
    customer: Customer = Relationship()
    employee_id: int = Field(foreign_key="employee.id")
    employee: Employee = Relationship()


class SaleItem(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    quantity: int
    discount: float
    is_gift: bool
    notes: Optional[str]

    sale_id: int = Field(foreign_key="sale.id")
    sale: Sale = Relationship(back_populates="items")
    edition_id: str = Field(foreign_key="edition.isbn")
    edition: Edition = Relationship()
