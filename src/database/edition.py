from src.models import Edition
from .infra import engine
from sqlmodel import Session, select, func, col
from typing import Optional


def filter_editions(
    page: int,
    size: int,
    isbn: Optional[str] = None,
    price: Optional[float] = None,
    publisher: Optional[str] = None,
    language: Optional[str] = None,
    publication_year: Optional[int] = None,
    stock: Optional[int] = None,
    book_id: Optional[int] = None,
):
    with Session(engine) as session:
        statement = (
            select(Edition)
            .where(isbn == None or Edition.isbn == isbn)
            .where(price == None or Edition.price == price)
            .where(publisher == None or publisher.lower() in Edition.publisher.lower())
            .where(language == None or language.lower() in Edition.language.lower())
            .where(
                publication_year == None or Edition.publication_year == publication_year
            )
            .where(stock == None or Edition.stock == stock)
            .where(book_id == None or Edition.book_id == book_id)
        )

        statement = statement.offset((page - 1) * size).limit(size)

        return session.exec(statement).all()


def count():
    with Session(engine) as session:
        statement = select(func.count(col(Edition.isbn)))

        return session.exec(statement).one()
