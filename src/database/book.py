from src.models import Book
from .infra import engine
from sqlmodel import Session, select
from typing import Optional
from datetime import date

def filter_books(
    id: Optional[int] = None,
    title: Optional[str] = None,
    publication_date: Optional[date] = None,
    language: Optional[str] = None,
    authors: Optional[str] = None,
    genres: Optional[str] = None
):
    with Session(engine) as session:
        statement = select(Book) \
            .where(id == None or Book.id == id) \
            .where(title == None or Book.title == title) \
            .where(publication_date == None or Book.publication_date == publication_date) \
            .where(language == None or Book.language == language) \
            .where(authors == None or Book.authors == authors) \
            .where(genres == None or Book.genres == genres)
        
        return session.exec(statement).all()