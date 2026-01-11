from pydantic import BaseModel
from typing import List

from app.db.models.ledger_models import AccountType
from app.schemas.ledger_schema import LedgerRead


class LedgerGroupTree(BaseModel):
    id:int
    name:str
    account_type:AccountType
    children:List["LedgerGroupTree"]
    ledgers:List["LedgerRead"]

    class config:
        orm_mode=True 


LedgerGroupTree.model_rebuild()
