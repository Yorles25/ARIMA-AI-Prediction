# backend/migrate_data.py
import asyncio
from backend.db import engine, Base, SessionLocal
from backend.models import HistoricalData

# Datos históricos reales
historical_data = [
    {"FECHA": "2024-10-31", "MD": 97, "TD": 85, "NC": 47},
    {"FECHA": "2024-10-30", "MD": 59, "TD": 44, "NC": 74},
    {"FECHA": "2024-10-29", "MD": 31, "TD": 69, "NC": 34},
    {"FECHA": "2024-10-28", "MD": 26, "TD": 58, "NC": 15},
    {"FECHA": "2024-10-27", "MD": 9,  "TD": 73, "NC": 83},
    {"FECHA": "2024-10-26", "MD": 60, "TD": 63, "NC": 7},
    {"FECHA": "2024-10-25", "MD": 75, "TD": 36, "NC": 63},
    {"FECHA": "2024-10-24", "MD": 32, "TD": 21, "NC": 79},
    {"FECHA": "2024-10-23", "MD": 27, "TD": 64, "NC": 48},
    {"FECHA": "2024-10-22", "MD": 41, "TD": 99, "NC": 82},
]

async def init_db():
    # Crear tablas
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

    # Insertar datos
    async with SessionLocal() as session:
        for record in historical_data:
            row = HistoricalData(
                fecha=record["FECHA"],
                md=record["MD"],
                td=record["TD"],
                nc=record["NC"]
            )
            session.add(row)
        await session.commit()

if __name__ == "__main__":
    asyncio.run(init_db())
