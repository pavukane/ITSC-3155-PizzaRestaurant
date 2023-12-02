from . import orders, crusts, toppings


def load_routes(app):
    app.include_router(orders.router)
    app.include_router(crusts.router)
    app.include_router(toppings.router)

