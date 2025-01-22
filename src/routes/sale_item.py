from ..models import SaleItem
from ..db import get_db
from fastapi_crudrouter import SQLAlchemyCRUDRouter

sale_item_router = SQLAlchemyCRUDRouter(
    schema=SaleItem,
    db_model=SaleItem,
    db=get_db
)

@sale_item_router.get("")
def get_sale_items():
    return ""