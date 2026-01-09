from fastapi import APIRouter,Depends


from app.auth.dependencies import get_current_user



router = APIRouter(prefix="/ledger",dependencies=[Depends(get_current_user)])


