from ..models import Sale
from ..database.infra import get_db
from fastapi_crudrouter import SQLAlchemyCRUDRouter

sale_router = SQLAlchemyCRUDRouter(
    schema=Sale,
    db_model=Sale,
    db=get_db
)

@sale_router.get("")
def get_sales():
    return ""