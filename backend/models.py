# backend/models.py
from sqlalchemy import Column, Integer, String, Date
from .db import Base

class HistoricalData(Base):
    __tablename__ = "historical_data"
    id = Column(Integer, primary_key=True, index=True)
    fecha = Column(String, nullable=False)  # o Date si quieres
    md = Column(Integer, nullable=False)
    td = Column(Integer, nullable=False)
    nc = Column(Integer, nullable=False)
