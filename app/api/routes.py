from fastapi import APIRouter
from app.api.user_routes import router as user_router
from app.api.auth_routes import router as auth_router
from app.api.ledger_routes import router as ledger_router
from app.api.ledger_groups_routes import router as ledger_group_router
from app.api.ledger_tree_routes import router as ledger_tree_router



router = APIRouter(prefix='/api')


router.include_router(user_router)
router.include_router(auth_router)
router.include_router(ledger_router)
router.include_router(ledger_group_router)
router.include_router(ledger_tree_router)