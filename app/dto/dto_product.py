from typing import List, Optional
from pydantic import BaseModel
from .dto_common import OutputStatus,OutputBase


class Product(BaseModel):
    image: str
    productId: str
    productName: str
    price: int
    amount: int

class OutputGetProduct(OutputStatus):
    data : Optional[List[Product]] = []

class InputUpdateStock(BaseModel):
    updateStock : int
