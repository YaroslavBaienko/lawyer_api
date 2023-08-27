from fastapi import APIRouter, Depends, HTTPException
from db.database import database
from db.models import Client as DBClient
from schemas.clients import ClientCreate, Client, ClientInDB
from typing import List

router = APIRouter()


# Database operations
async def create_new_client(client_data: ClientCreate) -> Client:
    existing_client = await fetch_client_by_telegram_id(client_data.note)
    if existing_client:
        raise ValueError("Client with the same note already exists.")

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
    except ValueError as ve:
        raise HTTPException(status_code=400, detail=str(ve))
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error occurred: {e}")


@router.get("/", response_model=List[ClientInDB])
async def get_all_clients():
    try:
        return await fetch_all_clients()
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error occurred: {e}")


async def fetch_client_by_telegram_id(telegram_id: str) -> ClientInDB:
    # Assuming DBClient has a field called telegram_id for storing the user's Telegram ID.
    query = DBClient.__table__.select().where(DBClient.note == telegram_id)
    return await database.fetch_one(query)


@router.get("/{telegram_id}")
async def get_client_data(telegram_id: str):
    try:
        client_data = await fetch_client_by_telegram_id(telegram_id)
        if client_data:
            return client_data  # Return the entire client data
        else:
            # If the client is not registered, return a clear indication of that
            return {"error": "Client not registered"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error occurred: {e}")
