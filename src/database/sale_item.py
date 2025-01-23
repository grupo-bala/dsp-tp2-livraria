from src.models import SaleItem
from .infra import engine
from sqlmodel import Session, select
from typing import Optional


def filter_sale_items(
    page: int,
    size: int,
    id: Optional[int] = None,
    quantity: Optional[int] = None,
    discount: Optional[float] = None,
    is_gift: Optional[bool] = None,
    notes: Optional[str] = None,
    sale_id: Optional[int] = None,
    edition_id: Optional[int] = None,
):
    with Session(engine) as session:
        statement = select(SaleItem) \
            .where(id == None or SaleItem.id == id) \
            .where(quantity == None or SaleItem.quantity == quantity) \
            .where(discount == None or SaleItem.discount == discount) \
            .where(is_gift == None or SaleItem.is_gift == is_gift) \
            .where(notes == None or notes.lower() in SaleItem.notes.lower()) \
            .where(sale_id == None or SaleItem.sale_id == sale_id) \
            .where(edition_id == None or SaleItem.edition_id == edition_id)
        
        statement = statement.offset((page - 1) * size).limit(size)
        
        return session.exec(statement).all()