from fastapi import APIRouter, Depends, HTTPException
from db.database import database
from db.models import Judge as DBJudge
from typing import List
from schemas.judges import JudgeCreate, Judge

router = APIRouter()


# Database operations
async def create_new_judge(judge_data: JudgeCreate) -> Judge:
    query = DBJudge.__table__.insert().values(**judge_data.dict())
    judge_id = await database.execute(query)
    return {**judge_data.dict(), "id": judge_id}


async def update_judge_phone_by_name(name_surname: str, phone: str) -> Judge:
    query = DBJudge.__table__.select().where(DBJudge.name_surname.ilike(f"%{name_surname}%"))
    existing_judge = await database.fetch_one(query)
    if not existing_judge:
        raise HTTPException(status_code=404, detail="Judge not found")
    update_query = (
        DBJudge.__table__.update()
        .where(DBJudge.name_surname.ilike(f"%{name_surname}%"))
        .values(phone=phone)
    )
    await database.execute(update_query)
    updated_judge_query = DBJudge.__table__.select().where(DBJudge.name_surname.ilike(f"%{name_surname}%"))
    return await database.fetch_one(updated_judge_query)


async def fetch_all_judges() -> List[Judge]:
    query = DBJudge.__table__.select()
    return await database.fetch_all(query)


async def fetch_judge_by_surname(name_surname: str) -> Judge:
    query = DBJudge.__table__.select().where(DBJudge.name_surname.ilike(f"%{name_surname}%"))
    return await database.fetch_one(query)


# Routes
@router.post("/", response_model=Judge)
async def create_judge(judge: JudgeCreate):
    return await create_new_judge(judge)


@router.put("/{name_surname}/update-phone", response_model=Judge)
async def update_judge_phone(name_surname: str, phone: str):
    return await update_judge_phone_by_name(name_surname, phone)


@router.get("/", response_model=List[Judge])
async def get_all_judges():
    return await fetch_all_judges()


@router.get("/{name_surname}")
async def get_judge_by_surname(name_surname: str):
    judge = await fetch_judge_by_surname(name_surname)
    if not judge:
        raise HTTPException(status_code=404, detail="Judge not found")
    return judge
