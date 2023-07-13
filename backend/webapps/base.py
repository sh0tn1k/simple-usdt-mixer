from fastapi import APIRouter
from webapps import route_general_pages


api_router = APIRouter()
api_router.include_router(route_general_pages.router,prefix="", tags=["Главная страница"])
