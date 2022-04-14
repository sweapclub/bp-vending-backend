from typing import List, Optional
from pydantic import BaseModel
from .dto_common import OutputStatus


class Report(BaseModel):
    reportTs: str
    productName: str
    productPrice: int
    amount: int
    takeMoney: int
    change: int


class OutputReport(OutputStatus):
    data: Optional[List[Report]] = []
