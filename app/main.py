from fastapi import FastAPI, Depends, HTTPException
from db.database import engine, Base, SessionLocal
from fastapi.templating import Jinja2Templates
from starlette.requests import Request
from api import clients, judges
from fastapi.staticfiles import StaticFiles
from starlette.responses import RedirectResponse
import uvicorn
import logging

# Setting up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI()

templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")

# Creating database tables
try:
    Base.metadata.create_all(bind=engine)
    logger.info("Database tables created successfully.")
except Exception as e:
    logger.error(f"Error creating database tables: {e}")


@app.get("/")
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


app.include_router(clients.router, prefix="/clients", tags=["clients"])
app.include_router(judges.router, prefix="/judges", tags=["judges"])


