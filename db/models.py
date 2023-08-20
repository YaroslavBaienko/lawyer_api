from sqlalchemy import Column, Integer, String, Boolean
from db.database import Base


class BaseModel(Base):
    __abstract__ = True

    # Convert model instance to dictionary
    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}


class Client(BaseModel):
    __tablename__ = "clients"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), unique=True, index=True)  # Added length constraint
    phone = Column(String(15), index=True)  # Added length constraint for phone number
    email = Column(String(100), index=True, nullable=False)  # Made email not nullable
    note = Column(String(300), index=True)  # Added length constraint
    is_admin = Column(Boolean, default=False)
    hashed_password = Column(String)


class Judge(BaseModel):
    __tablename__ = "judges"

    id = Column(Integer, primary_key=True, index=True)
    name_surname = Column(String(200), index=True)  # Added length constraint
    court = Column(String(200), index=True)  # Added length constraint
    phone = Column(String(15), index=True)  # Added length constraint for phone number
    email = Column(String(100), index=True, nullable=False)  # Made email not nullable
    note = Column(String(300), index=True)  # Added length constraint
