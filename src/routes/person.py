from ..models import Person
from ..database.infra import get_db
from fastapi_crudrouter import SQLAlchemyCRUDRouter

people_router = SQLAlchemyCRUDRouter(
    schema=Person,
    db_model=Person,
    db=get_db
)

@people_router.get("")
def get_people():
    return ""