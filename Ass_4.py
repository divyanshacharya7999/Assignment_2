class MenuItem:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f"{self.name} - {self.price:.2f}"

class Food(MenuItem):
    def __init__(self, name, price, description):
        super().__init__(name, price)
        self.description = description

    def __str__(self):
        return f"{super().__str__()} ({self.description})"

class Drink(MenuItem):
    def __init__(self, name, price, description):
        super().__init__(name, price)
        self.description = description

    def __str__(self):
        return f"{super().__str__()} ({self.description})"

class Menu:
    def __init__(self):
        self.menu_items = []

    def add_item(self, menu_item):
        self.menu_items.append(menu_item)

    def remove_item(self, name):
        self.menu_items = [item for item in self.menu_items if item.name != name]

    def display_menu(self):
        print("Menu:")
        for item in self.menu_items:
            print(item)

class Restaurant:
    def __init__(self):
        self.menu = Menu()

    def add_menu_item(self, menu_item):
        self.menu.add_item(menu_item)

    def remove_menu_item(self, name):
        self.menu.remove_item(name)

    def display_menu(self):
        self.menu.display_menu()

    def calculate_total_cost(self, order):
        return sum(item.price for item in order)

    def place_order(self):
        order = []
        self.display_menu()
        while True:
            action = input("Enter 'add' to add an item, 'remove' to remove an item, or 'done' to finish: ").lower()
            if action == 'done':
                break
            elif action == 'add':
                item_name = input("Enter the name of the item you want to add: ")
                for item in self.menu.menu_items:
                    if item.name == item_name:
                        order.append(item)
                        print(f"Added {item_name} to your order.")
                        break
                else:
                    print("Item not found on the menu.")
            elif action == 'remove':
                item_name = input("Enter the name of the item you want to remove: ")
                for item in order:
                    if item.name == item_name:
                        order.remove(item)
                        print(f"Removed {item_name} from your order.")
                        break
                else:
                    print("Item not found in your order.")
            else:
                print("Invalid action. Please enter 'add', 'remove', or 'done'.")
        return order

restaurant = Restaurant()

restaurant.add_menu_item(Food("Pizza", 200, "Onion Pizza"))
restaurant.add_menu_item(Drink("Cola", 60, "Coca-Cola"))
restaurant.add_menu_item(Drink("Wine", 500, "Budweiser"))

order = restaurant.place_order()

total_cost = restaurant.calculate_total_cost(order)
print(f"Total cost of the order: {total_cost:.2f}")
