from fastapi import FastAPI
from .routes.book import book_router
from .routes.edition import edition_router
from .routes.person import people_router
from .routes.sale import sale_router
from .routes.sale_item import sale_item_router

app = FastAPI()

app.include_router(book_router)
app.include_router(edition_router)
app.include_router(sale_router)
app.include_router(people_router)
app.include_router(sale_item_router)