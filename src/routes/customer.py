from ..models import Customer
from ..database.infra import get_db
from fastapi_crudrouter import SQLAlchemyCRUDRouter

customer_router = SQLAlchemyCRUDRouter(
    schema=Customer,
    db_model=Customer,
    db=get_db
)

@customer_router.get("")
def get_customers():
    return ""