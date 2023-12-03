from datetime import datetime
from typing import Optional
from pydantic import BaseModel
from .crusts import Crust
from .toppings import Topping


class PizzaBase(BaseModel):
    toppings: list[int] = []
    crusts: list[int] = []


class PizzaCreate(PizzaBase):
    pass


class PizzaUpdate(BaseModel):
    toppings: list[int] = []
    crusts: list[int] = []


class Pizza(PizzaBase):
    id: int
    price: float
    toppings: list[Topping] = None
    crusts: list[Crust] = None

    class ConfigDict:
        from_attributes = True
