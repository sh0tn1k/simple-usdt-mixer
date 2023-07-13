import datetime
from typing import Optional
from pydantic import BaseModel


class TransactionCreate(BaseModel):
    hash: Optional[str] = None
    amount: Optional[int] = None
    date: datetime = None
    type: Optional[str] = None
    status: Optional[str] = None
    owner_id: Optional[int] = None
    owner_name: Optional[str] = None

    class Config():
        orm_mode = True
