from datetime import datetime
from typing import Optional
from pydantic import BaseModel
from .pizzas import Pizza


class OrderBase(BaseModel):
    customer_name: str
    pizzas: list[int] = []


class OrderCreate(OrderBase):
    pass


class OrderUpdate(BaseModel):
    customer_name: Optional[str] = None


class Order(OrderBase):
    id: int
    order_date: Optional[datetime] = None
    pizzas: list[Pizza] = None

    class ConfigDict:
        from_attributes = True
