from fastapi import Depends, FastAPI
from .routers import products, payments, report
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

version_prefix = "/api/v1"

app.include_router(
    products.router,
    prefix=version_prefix
)

app.include_router(
    payments.router,
    prefix=version_prefix
)

app.include_router(
    report.router,
    prefix=version_prefix
)