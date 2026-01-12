from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.db.models.ledger_models import Ledger,LedgerGroup
from app.schemas.Ledgers.ledger_schema import LedgerCreate


def get_all_ledgers(db:Session,user_id:int):
    return db.query(Ledger).filter(
        (Ledger.is_active) & ((Ledger.user_id==user_id) | (Ledger.is_system) )
    ).all()


def create_ledger(db:Session,user_id:int,data:LedgerCreate):

    ledger_group = db.get(LedgerGroup,data.group_id)

    if not ledger_group:
        raise HTTPException(status_code=404,detail="Group not found")
    
    my_ledger = Ledger(
        name = data.name,
        group_id = data.group_id,
        user_id = user_id,
        opening_balance = data.opening_balance,
        opening_balance_type = data.opening_balance_type,
        is_system = False
    )

    db.add(my_ledger)
    db.commit()
    db.refresh(my_ledger)
    return my_ledger


def get_ledgers_by_group(db:Session,user_id:int,group_id:int):
    return db.query(Ledger).filter(
        Ledger.group_id == group_id,
        (Ledger.is_active) & ((Ledger.user_id==user_id) | (Ledger.is_system))
    ).all()