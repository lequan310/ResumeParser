from fastapi import APIRouter

from api.v1.endpoints.analysis import router as analysis_router
from api.v1.endpoints.chat import router as chat_router
from api.v1.endpoints.files import router as files_router

routers = APIRouter(prefix="/api/v1", tags=["V1"])
router_list = [files_router, chat_router, analysis_router]

for router in router_list:
    router.tags.append("v1")
    routers.include_router(router)
