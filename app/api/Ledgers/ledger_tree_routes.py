from fastapi import APIRouter,Depends
from sqlalchemy.orm import Session
from typing import List

from app.db.session import get_db
from app.auth.dependencies import get_current_user

from app.db.models.user_models import User
from app.schemas.Ledgers.ledger_tree_schema import LedgerGroupTree

from app.services.Ledgers.ledger_tree_service import get_group_tree


router=APIRouter(prefix="/ledger-tree",tags=["ledger-tree"])


@router.get("/tree",response_model=List[LedgerGroupTree])
def chart_of_accounts_tree(db:Session=Depends(get_db),current_user:User=Depends(get_current_user)):
    return get_group_tree(db,current_user.id)
