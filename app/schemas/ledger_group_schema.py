from pydantic import BaseModel
from app.db.models.ledger_models import AccountType
from typing import Optional



class LedgerGroupCreate(BaseModel):
    name:str
    parent_id:int
    

class LedgerGroupRead(BaseModel):
    id:int
    name:str
    account_type:AccountType
    parent_id:Optional[int] 
    is_system:bool

    class config:
        orm_mode=True 

