# backend/migrate_data.py
import asyncio
from sqlalchemy.ext.asyncio import AsyncSession
from .db import engine, Base, SessionLocal
from .models import HistoricalData

# Datos históricos de ejemplo (puedes cambiarlos después)
historical_data = [
    {"date": "2025-09-20", "value": 42.5},
    {"date": "2025-09-21", "value": 43.1},
    {"date": "2025-09-22", "value": 44.8},
    {"date": "2025-09-23", "value": 45.2},
]

async def init_db():
    # Crear tablas
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

    # Insertar datos
    async with SessionLocal() as session:
        for record in historical_data:
            row = HistoricalData(date=record["date"], value=record["value"])
            session.add(row)
        await session.commit()

if __name__ == "__main__":
    asyncio.run(init_db())
