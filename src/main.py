import sys
from fastapi import FastAPI, Request
from loguru import logger
from .routes.book import book_router
from .routes.edition import edition_router
from .routes.customer import people_router
from .routes.sale import sale_router
from .routes.sale_item import sale_item_router
from .routes.employee import employees_router


LOGGER_FORMAT = (
    "<green>{time:YYYY-MM-DD HH:mm:ss.SSS}</green> | "
    "<level>{level: <8}</level> | "
    "<cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> | "
    "<level>{message} - Additional information: {extra}</level>"
)

logger.remove()
logger.add(sys.stderr, format=LOGGER_FORMAT)
logger.add("actions.log")

app = FastAPI()

@app.middleware("http")
async def log_requests(request: Request, call_next):
    inner_log = logger
    inner_log.info(f"Receiving request: {request.method} {request.url}")
   
    response = None

    try:
        response = await call_next(request)
        inner_log.info(f"Response: {response.status_code}")
    except Exception as error:
        inner_log.error(f"Response: 500")
        raise error
    
    return response


app.include_router(book_router)
app.include_router(edition_router)
app.include_router(sale_router)
app.include_router(people_router)
app.include_router(sale_item_router)
app.include_router(employees_router)