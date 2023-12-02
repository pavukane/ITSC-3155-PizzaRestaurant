from fastapi import APIRouter, Depends, FastAPI, status, Response
from sqlalchemy.orm import Session
from ..controllers import crusts as controller
from ..schemas import crusts as schema
from ..dependencies.database import engine, get_db

router = APIRouter(
    tags=['Crusts'],
    prefix="/crusts"
)


@router.get("/", response_model=list[schema.Crust])
def read_all(db: Session = Depends(get_db)):
    return controller.read_all(db)


@router.get("/{item_id}", response_model=schema.Crust)
def read_one(item_id: int, db: Session = Depends(get_db)):
    return controller.read_one(db, item_id=item_id)

