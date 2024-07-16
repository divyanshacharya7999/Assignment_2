from menu import Menu, Food, Drink
from order import Order
from exceptions import MenuItemNotFoundException, OrderItemNotFoundException

class Restaurant:
    def __init__(self):
        self.menu = Menu()

    def add_menu_item(self, menu_item):
        self.menu.add_item(menu_item)

    def remove_menu_item(self, name):
        self.menu.remove_item(name)

    def display_menu(self):
        self.menu.display_menu()

    def place_order(self):
        order = Order()
        self.display_menu()

        while True:
            action = input("Enter 'add' to add an item, 'remove' to remove an item, or 'done' to finish: ").lower()
            if action == 'done':
                break
            elif action == 'add':
                item_name = input("Enter the name of the item you want to add: ")
                try:
                    item = self.menu.get_item_by_name(item_name)
                    order.add_item(item)
                    print(f"Added {item_name} to your order.")
                except MenuItemNotFoundException as e:
                    print(e)
            elif action == 'remove':
                item_name = input("Enter the name of the item you want to remove: ")
                try:
                    order.remove_item(item_name)
                    print(f"Removed {item_name} from your order.")
                except OrderItemNotFoundException as e:
                    print(e)
            else:
                print("Invalid action. Please enter 'add', 'remove', or 'done'.")
        
        return order
