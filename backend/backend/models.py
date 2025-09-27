# backend/models.py
from sqlalchemy import Column, Integer, Float, String
from .db import Base

class HistoricalData(Base):
    __tablename__ = "historical_data"

    id = Column(Integer, primary_key=True, index=True)
    date = Column(String, index=True)   # en el futuro lo cambiamos a Date
    value = Column(Float)
