from sqlalchemy.orm import sessionmaker
from db.database import engine, Base
from db.models import Judge as DBJudge

import pandas as pd
from pathlib import Path

# Get the current script's directory as a Path object
current_directory = Path(__file__).parent

# Get the parent directory
parent_directory = current_directory.parent

Base.metadata.create_all(bind=engine)
Session = sessionmaker(bind=engine)
session = Session()

df = pd.read_excel(f"{parent_directory}\judges.xlsx")
for _, row in df.iterrows():
    # Convert NaN values to empty string for 'email' and 'note' columns
    email = '' if pd.isna(row.get('email')) else row.get('email')
    note = '' if pd.isna(row.get('note')) else row.get('note')

    judge = DBJudge(
        name_surname=row.get('name_surname'),
        court=row.get('court'),
        phone=row.get('phone'),
        email=email,
        note=note
    )
    session.add(judge)
    session.commit()
    session.close()
