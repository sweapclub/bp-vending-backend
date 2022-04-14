from typing import List, Optional
from pydantic import BaseModel
from .dto_common import OutputStatus, OutputBase


# class Product(BaseModel):
#     productId: str
#     productName: str
#     price: int
#     amount: int


# class OutputGetProduct(OutputStatus):
#     data: Optional[List[Product]] = []


# class InputUpdateStock(BaseModel):
#     updateStock: int


class Wallet(BaseModel):
    coin_1: int
    coin_5: int
    coin_10: int
    bank_20: int
    bank_50: int
    bank_100: int
    bank_500: int
    bank_1000: int


class OutputGetWallet(OutputStatus):
    data: Optional[Wallet]

class InputPayment(BaseModel):
    productId: str
    amount: int
    money: int
    moneyDetail: Wallet

class ChangeDetail(BaseModel):
    toc : str
    amount : int

class OutputPayment(OutputStatus):
    data: Optional[List[ChangeDetail]] = []
    suggestion : List[str] = []