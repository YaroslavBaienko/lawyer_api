import os
from sqlalchemy import create_engine, MetaData, exc
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from databases import Database

# Fetch the database URL from environment variables or use a default value.
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./test.db")

# Create SQLAlchemy engine to interact with the database.
# echo=True enables logging, and pool_size & max_overflow are for connection pooling.
# Create SQLAlchemy engine to interact with the database.
# echo=True enables logging.
try:
    engine = create_engine(DATABASE_URL, echo=True)
except exc.SQLAlchemyError as err:
    print(f"Error while creating the database engine: {err}")

# Create metadata instance for SQLAlchemy.
metadata = MetaData()

# Create an instance for asynchronous database interactions.
database = Database(DATABASE_URL)

# Provide a base model for SQLAlchemy to declare models.
Base = declarative_base()

# For synchronous operations, we'll use a session.
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)
