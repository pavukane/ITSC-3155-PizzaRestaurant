from datetime import datetime
from typing import Optional
from pydantic import BaseModel


class ToppingBase(BaseModel):
    name: str
    price: float


class Topping(ToppingBase):
    id: int

    class ConfigDict:
        from_attributes = True
