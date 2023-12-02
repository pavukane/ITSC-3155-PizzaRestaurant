from sqlalchemy.orm import Session
from fastapi import HTTPException, status, Response, Depends
from ..models import toppings as model
from sqlalchemy.exc import SQLAlchemyError


def read_all(db: Session):
    try:
        result = db.query(model.Topping).all()
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)
    return result


def read_one(db: Session, item_id):
    try:
        item = db.query(model.Topping).filter(model.Topping.id == item_id).first()
        if not item:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Id not found!")
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)
    return item

