from src.models import Book
from .infra import engine
from sqlmodel import Session, select
from typing import Optional
from datetime import date


def filter_books(
    page: int,
    size: int,
    id: Optional[int] = None,
    title: Optional[str] = None,
    publication_date: Optional[date] = None,
    language: Optional[str] = None,
    author: Optional[str] = None,
    genre: Optional[str] = None
):
    with Session(engine) as session:
        statement = select(Book) \
            .where(id == None or Book.id == id) \
            .where(title == None or title.lower() in Book.title.lower()) \
            .where(publication_date == None or Book.publication_date == publication_date) \
            .where(language == None or language.lower() in Book.language.lower()) \
            .where(author == None or author.lower() in Book.author.lower()) \
            .where(genre == None or genre.lower() in Book.genre.lower())
        
        statement = statement.offset((page - 1) * size).limit(size)
        
        return session.exec(statement).all()