from datetime import datetime
from typing import Optional
from pydantic import BaseModel
from .order_details import OrderDetail


class CrustBase(BaseModel):
    name: str
    price: float


class Crust(CrustBase):
    id: int

    class ConfigDict:
        from_attributes = True
