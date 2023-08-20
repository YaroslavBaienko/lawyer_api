from pydantic import BaseModel
from typing import Optional


# Base Pydantic model for judges. Defines the common attributes.
class JudgeBase(BaseModel):
    name_surname: str
    court: str
    phone: str
    email: Optional[str] = None
    note: Optional[str] = None


# Pydantic model for creating a new judge. Can be extended with additional attributes or validations.
class JudgeCreate(JudgeBase):
    pass


# Pydantic model to represent a judge fetched from the database or for API responses.
class Judge(JudgeBase):
    id: int
