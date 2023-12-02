from . import orders, crusts


def load_routes(app):
    app.include_router(orders.router)
    app.include_router(crusts.router)

