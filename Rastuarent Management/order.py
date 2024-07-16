from exceptions import OrderItemNotFoundException

class Order:
    def __init__(self):
        self.order_items = []

    def add_item(self, item):
        self.order_items.append(item)

    def remove_item(self, name: str):
        for item in self.order_items:
            if item.name == name:
                self.order_items.remove(item)
                return
        raise OrderItemNotFoundException(f"Order item '{name}' not found.")

    def calculate_total(self):
        return sum(item.price for item in self.order_items)

    def display_order(self):
        print("Order Details:")
        for item in self.order_items:
            print(item)
