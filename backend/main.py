from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from core.config import settings
from fastapi.templating import Jinja2Templates
from webapps.base import api_router as web_app_router
from starlette.exceptions import HTTPException as StarletteHTTPException
from db.session import engine
from db.base import Base 
from db.utils import check_db_connected,check_db_disconnected

templates = Jinja2Templates(directory="templates")

def include_router(app):
    app.include_router(web_app_router)

# Обслуживание файлов css и другого барахла для фронтенда
def configure_static(app):
    app.mount("/static", StaticFiles(directory="static"), name="static")

# Создание таблиц из /db/models в бд
def create_tables():
	  Base.metadata.create_all(bind=engine)

def start_application():
  app = FastAPI(title=settings.PROJECT_NAME,version=settings.PROJECT_VERSION)
  include_router(app)
  configure_static(app)
  create_tables()
  return app 

app = start_application()

@app.on_event("startup")
async def app_startup():
    await check_db_connected()

@app.on_event("shutdown")
async def app_shutdown():
    await check_db_disconnected()