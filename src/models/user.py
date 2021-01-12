import datetime

from sqlalchemy import (
    Column,
    Integer,
    String,
    DateTime,
)

from src.models.db import Base


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, autoincrement=True)
    uid = Column(Integer, unique=True, nullable=False)
    first_name = Column(String(32))
    last_name = Column(String(32))
    created_at = Column(DateTime, default=datetime.datetime.now)

    def __repr__(self):
        return f'<User: {self.uid}>'
