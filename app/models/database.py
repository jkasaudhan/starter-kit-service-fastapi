from sqlmodel import SQLModel, create_engine
from app.core.config import settings

engine = create_engine(
    settings.DATABASE_URL, 
    connect_args={"check_same_thread": False} if settings.DATABASE_URL.startswith("sqlite") else {}
)

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)