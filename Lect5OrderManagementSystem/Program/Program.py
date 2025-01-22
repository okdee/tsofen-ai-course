from Core.Domain.Order.Models.Order import Order
from Core.Domain.Product.Models.Product import Product


def main():
    order1 = Order("order1", "Omar Gharra", [Product("PlayStation", 2, 1200.0)])
    order1.display_order()
    print(order1.calculate_total())
    order1.update_quantity("PlayStation",3)
    print(order1.calculate_total())

if __name__ == "__main__":
    main()