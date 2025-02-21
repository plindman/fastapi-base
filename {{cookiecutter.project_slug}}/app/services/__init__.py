''' services parent module '''
from fastapi import APIRouter

# from fastapi import Security
# from ..core.auth_api_key import  verify_api_key
# router = APIRouter(dependencies=[Security(verify_api_key)])
router = APIRouter(tags=["Services"], prefix="/api/v1")

from .sample_service import router as data_router
router.include_router(data_router)
