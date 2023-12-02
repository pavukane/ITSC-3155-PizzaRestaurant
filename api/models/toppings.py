from sqlalchemy import Column, ForeignKey, Integer, String, DECIMAL, DATETIME
from sqlalchemy.orm import relationship
from datetime import datetime
from ..dependencies.database import Base


class Topping(Base):
    __tablename__ = "toppings"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String(50), index=True)
    price = Column(DECIMAL(10, 2), nullable=False, server_default='0.0')


