from fastapi import APIRouter, Depends, HTTPException
from db.database import database
from db.models import Client as DBClient
from schemas.clients import ClientCreate, Client, ClientInDB
from typing import List

router = APIRouter()


# Database operations
async def create_new_client(client_data: ClientCreate) -> Client:
    query = DBClient.__table__.insert().values(**client_data.dict())
    client_id = await database.execute(query)
    return {**client_data.dict(), "id": client_id}


async def fetch_all_clients() -> List[ClientInDB]:
    query = DBClient.__table__.select()
    return await database.fetch_all(query)


# Routes
@router.post("/", response_model=Client)
async def create_client(client: ClientCreate):
    try:
        return await create_new_client(client)
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error occurred: {e}")


@router.get("/", response_model=List[ClientInDB])
async def get_all_clients():
    try:
        return await fetch_all_clients()
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error occurred: {e}")
