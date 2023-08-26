from app.database.controller import SessionLocal, engine
from fastapi import APIRouter


router = APIRouter()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()