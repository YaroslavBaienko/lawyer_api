from pydantic import BaseModel
from typing import Optional


class ClientBase(BaseModel):
    name: str
    phone: str
    email: Optional[str] = None
    note: str
    is_admin: Optional[bool] = False


class ClientCreate(ClientBase):
    pass


# Model to represent a client fetched from the database
class ClientInDB(ClientCreate):
    id: int


class Client(ClientBase):
    id: int

    class Config:
        from_attributes = True
