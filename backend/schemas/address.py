from typing import Optional
from pydantic import BaseModel

class WalletCreate(BaseModel):
    name : Optional[str] = None
    private_key : Optional[str] = None
    public_key : Optional[str] = None
    hex_address : Optional[str] = None

class ShowWallet(BaseModel):

    class Config():
        orm_mode = True