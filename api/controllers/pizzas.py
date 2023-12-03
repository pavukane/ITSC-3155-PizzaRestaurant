from sqlalchemy.orm import Session
from fastapi import HTTPException, status, Response, Depends
from ..models import pizzas as model, crusts, toppings
from sqlalchemy.exc import SQLAlchemyError


def create(db: Session, request):
    price = 0

    toppings_data = []
    for topping_id in request.toppings:
        topping = db.query(toppings.Topping).where(toppings.Topping.id == topping_id).first()
        toppings_data.append(topping)
        price += topping.price

    crusts_data = []
    for crust_id in request.crusts:
        crust = db.query(crusts.Crust).where(crusts.Crust.id == crust_id).first()
        crusts_data.append(crust)
        price += crust.price

    new_pizza = model.Pizza(price=price)
    new_pizza.toppings = toppings_data
    new_pizza.crusts = crusts_data

    try:
        db.add(new_pizza)
        db.commit()
        db.refresh(new_pizza)
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)

    return new_pizza


def read_all(db: Session):
    try:
        result = db.query(model.Pizza).all()
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)
    return result


def read_one(db: Session, item_id):
    try:
        item = db.query(model.Pizza).filter(model.Pizza.id == item_id).first()
        if not item:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Id not found!")
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)
    return item


def update(db: Session, item_id, request):
    try:
        item = db.query(model.Pizza).filter(model.Pizza.id == item_id)
        if not item.first():
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Id not found!")
        update_data = request.dict(exclude_unset=True)
        item.update(update_data, synchronize_session=False)
        db.commit()
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)
    return item.first()


def delete(db: Session, item_id):
    try:
        item = db.query(model.Pizza).filter(model.Pizza.id == item_id)
        if not item.first():
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Id not found!")
        item.delete(synchronize_session=False)
        db.commit()
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)
    return Response(status_code=status.HTTP_204_NO_CONTENT)
