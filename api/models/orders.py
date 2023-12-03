from sqlalchemy import Column, ForeignKey, Integer, String, DECIMAL, DATETIME, Table
from sqlalchemy.orm import relationship
from datetime import datetime
from ..dependencies.database import Base

order_pizza_association = Table(
    'order_pizza_association',
    Base.metadata,
    Column('order_id', Integer, ForeignKey('orders.id')),
    Column('pizza_id', Integer, ForeignKey('pizzas.id'))
)

class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    customer_name = Column(String(50), index=True)
    order_date = Column(DATETIME, nullable=False, server_default=str(datetime.now()))
    total_price = Column(Integer)

    pizzas = relationship("Pizza", secondary=order_pizza_association, backref="orders")
