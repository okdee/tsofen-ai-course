from typing import List

from Core.Domain.Product.Models.Product import Product


class Order:
    def __init__(self, order_id: str, customer_name: str, products: List[Product]):
        self.order_id = order_id
        self.customer_name = customer_name
        self.products = products

    def display_order(self):
        print(f"Order id: {self.order_id}, Customer name: {self.customer_name}, Products: {self.products}")

    def calculate_total(self):
        return sum(product.quantity * product.price for product in self.products)

    def update_quantity(self, product_name: str, new_quantity: int):
        for product in self.products:
            if product.name == product_name:
                self.products[self.products.index(product)] = Product(product_name, new_quantity, product.price)
                print(f"Quantity updated for product: {product.name}")
                return
            print(f"No product found with name: {product_name}")
