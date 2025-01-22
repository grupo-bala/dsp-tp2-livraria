from ..models import Edition
from ..db import get_db
from fastapi_crudrouter import SQLAlchemyCRUDRouter

edition_router = SQLAlchemyCRUDRouter(
    schema=Edition,
    db_model=Edition,
    db=get_db
)

@edition_router.get("")
def get_edtions():
    return ""