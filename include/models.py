from sqlalchemy import Column, String, DateTime, Integer
from sqlalchemy.sql import func
from .db import Base

class Pokemon(Base):
    __tablename__ = 'pokemons'
    # Adicione o autoincrement=False para impedir que o SQLAlchemy escreva "SERIAL"
    id = Column(Integer, primary_key=True, autoincrement=False)
    name = Column(String)
    type = Column(String)
    created_at = Column(DateTime, default=func.now())