# backend/db.py
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker, declarative_base

# URL de conexión (usuario, contraseña, host=postgres, puerto=5432, base=aidb)
DATABASE_URL = "postgresql+asyncpg://aiuser:aisecret@postgres:5432/aidb"

# Motor asincrónico de SQLAlchemy
engine = create_async_engine(DATABASE_URL, echo=True, future=True)

# Sesión asincrónica
SessionLocal = sessionmaker(
    engine, 
    class_=AsyncSession, 
    expire_on_commit=False
)

# Clase base para los modelos
Base = declarative_base()
