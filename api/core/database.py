from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

from api.core.config import settings

engine = create_engine(settings.DATABASE_URL)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

Base = declarative_base()


# ✅ ADD THIS
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
