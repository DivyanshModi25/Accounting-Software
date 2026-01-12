from pydantic import BaseModel
from decimal import Decimal


from app.db.models.ledger_models import BalanceType

class LedgerCreate(BaseModel):
    name:str 
    group_id:int
    opening_balance:Decimal = Decimal(0.00) 
    opening_balance_type:BalanceType = BalanceType.DEBIT

class LedgerRead(BaseModel):
    id:int
    name:str
    group_id:int
    opening_balance:Decimal
    opening_balance_type:BalanceType
    is_system:bool

    class config:
        orm_mode=True