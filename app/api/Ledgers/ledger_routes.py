from fastapi import APIRouter,Depends
from sqlalchemy.orm import Session


from app.auth.dependencies import get_current_user
from app.db.session import get_db

from app.db.models.user_models import User
from app.schemas.Ledgers.ledger_schema import LedgerRead,LedgerCreate

from app.services.Ledgers.ledger_service import get_all_ledgers,create_ledger,get_ledgers_by_group



router = APIRouter(prefix="/ledger",tags=["ledger"])




@router.get("/my-ledgers",response_model=list[LedgerRead])
def list_all_user_ledgers(current_user:User = Depends(get_current_user), db:Session = Depends(get_db)):
    return get_all_ledgers(db,current_user.id)


@router.get("/my-ledgers/{group_id}",response_model=list[LedgerRead])
def list_ledger_by_group(group_id:int, current_user:User = Depends(get_current_user), db:Session = Depends(get_db)):
    return get_ledgers_by_group(db,current_user.id,group_id)



@router.post("/create",response_model=LedgerRead)
def create(data:LedgerCreate,current_user:User = Depends(get_current_user), db:Session = Depends(get_db)):
    return create_ledger(db,current_user.id,data)

