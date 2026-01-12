from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.db.models.ledger_models import LedgerGroup
from app.schemas.Ledgers.ledger_group_schema import LedgerGroupCreate


def get_user_ledger_groups(db:Session,user_id:int):
    return db.query(LedgerGroup).filter(
        (LedgerGroup.user_id==user_id) | 
        (LedgerGroup.is_system)
    ).all()



def create_group(db:Session,user_id:int,data:LedgerGroupCreate):
    
    parent = db.get(LedgerGroup, data.parent_id)

    if not parent:
        raise HTTPException(status_code=400,detail="Invalid parent group")



    my_ledger_group = LedgerGroup(
        name = data.name,
        account_type = parent.account_type,
        parent_id = data.parent_id,
        user_id = user_id,
        is_system = False 
    )

    db.add(my_ledger_group)
    db.commit()
    db.refresh(my_ledger_group)
    return my_ledger_group