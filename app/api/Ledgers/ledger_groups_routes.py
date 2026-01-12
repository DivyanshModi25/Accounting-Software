from fastapi import APIRouter,Depends
from sqlalchemy.orm import Session

from app.auth.dependencies import get_current_user
from app.db.session import get_db


from app.services.Ledgers.ledger_group_services import get_user_ledger_groups,create_group


from app.schemas.Ledgers.ledger_group_schema import LedgerGroupRead,LedgerGroupCreate
from app.db.models.user_models import User



router = APIRouter(prefix="/ledger-groups",tags=["ledger-groups"])


@router.get("/",response_model=list[LedgerGroupRead])
def list_ledger_groups(current_user:User = Depends(get_current_user),db:Session=Depends(get_db)):
    return get_user_ledger_groups(db,current_user.id)


@router.post("/create",response_model=LedgerGroupRead)
def create(data:LedgerGroupCreate,current_user:User=Depends(get_current_user),db:Session=Depends(get_db)):
    return create_group(db,current_user.id,data)