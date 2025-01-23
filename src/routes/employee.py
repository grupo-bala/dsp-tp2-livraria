from ..models import Employee
from ..database.infra import get_db
from fastapi_crudrouter import SQLAlchemyCRUDRouter

employees_router = SQLAlchemyCRUDRouter(
    schema=Employee,
    db_model=Employee,
    db=get_db
)

@employees_router.get("")
def get_employees():
    return ""