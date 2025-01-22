from Core.Domain.Order.Models.Order import Order


class OrderManager:
    def __init__(self):
        self.orders: list[Order] = []

    def add_order(self, order: Order):
        self.orders.append(order)