from fastapi import Depends, FastAPI
from .routers import products, payments

app = FastAPI()


version_prefix = "/api/v1"

app.include_router(
    products.router,
    prefix=version_prefix
)

app.include_router(
    payments.router,
    prefix=version_prefix
)

