from sqlalchemy import Column, ForeignKey, Integer, String, DECIMAL, DATETIME, Table
from sqlalchemy.orm import relationship
from datetime import datetime
from ..dependencies.database import Base

pizza_topping_association = Table(
    'pizza_topping_association',
    Base.metadata,
    Column('pizza_id', Integer, ForeignKey('pizzas.id')),
    Column('topping_id', Integer, ForeignKey('toppings.id'))
)

pizza_crust_association = Table(
    'pizza_crust_association',
    Base.metadata,
    Column('pizza_id', Integer, ForeignKey('pizzas.id')),
    Column('crust_id', Integer, ForeignKey('crusts.id'))
)


class Pizza(Base):
    __tablename__ = "pizzas"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    price = Column(DECIMAL(4, 2), nullable=False, server_default='0.0')
    
    toppings = relationship("Topping", secondary=pizza_topping_association, backref="pizzas")
    crusts = relationship("Crust", secondary=pizza_crust_association, backref="pizzas")

    # orders = relationship("Order", back_populates="pizza")
