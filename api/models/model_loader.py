from . import orders, pizzas, crusts, toppings

from ..dependencies.database import engine


def index():
    orders.Base.metadata.create_all(engine)
    pizzas.Base.metadata.create_all(engine)
    crusts.Base.metadata.create_all(engine)
    toppings.Base.metadata.create_all(engine)
