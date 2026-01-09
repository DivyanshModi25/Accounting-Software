from fastapi import APIRouter
from app.api.user_routes import router as user_router
from app.api.auth_routes import router as auth_router



router = APIRouter(prefix='/api')


router.include_router(user_router)
router.include_router(auth_router)
    