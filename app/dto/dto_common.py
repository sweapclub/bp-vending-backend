from typing import Optional
from pydantic import BaseModel
    
class OutputBase(BaseModel):
    status: str

class OutputStatus(OutputBase):
    errorMessage: Optional[str]
