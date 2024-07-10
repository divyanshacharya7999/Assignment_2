# Base class for Menu Item
class MenuItem:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f"{self.name}: ${self.price:.2f}"

# Subclass for Food Item
class FoodItem(MenuItem):
    def __init__(self, name, price):
        super().__init__(name, price)
        self.category = "Food"

# Subclass for Drink Item
class DrinkItem(MenuItem):
    def __init__(self, name, price):
        super().__init__(name, price)
        self.category = "Drink"

# Restaurant Management System class
class Restaurant:
    def __init__(self):
        self.menu_items = []

    def add_menu_item(self, item):
        self.menu_items.append(item)
        print(f"Added {item.category} item: {item.name} - ${item.price:.2f}")

    def remove_menu_item(self, item_name):
        removed = False
        for item in self.menu_items:
            if item.name == item_name:
                self.menu_items.remove(item)
                print(f"Removed {item.category} item: {item.name}")
                removed = True
                break
        if not removed:
            print(f"Item '{item_name}' not found in the menu.")

    def display_menu(self):
        print("Menu:")
        for item in self.menu_items:
            print(f"{item.category}: {item.name} - ${item.price:.2f}")

    def calculate_total_cost(self, order_items):
        total_cost = 0.0
        for item_name in order_items:
            found = False
            for item in self.menu_items:
                if item.name == item_name:
                    total_cost += item.price
                    found = True
                    break
            if not found:
                print(f"Item '{item_name}' not found in the menu.")
        return total_cost

# Testing the restaurant management system
if __name__ == "__main__":
    restaurant = Restaurant()

    # Adding menu items
    restaurant.add_menu_item(FoodItem("Burger", 8.99))
    restaurant.add_menu_item(DrinkItem("Coke", 1.99))
    restaurant.add_menu_item(FoodItem("Pizza", 12.99))
    restaurant.add_menu_item(DrinkItem("Coffee", 2.99))

    # Displaying the menu
    restaurant.display_menu()

    # Removing a menu item
    restaurant.remove_menu_item("Coke")
    restaurant.display_menu()

    # Calculating the total cost of an order
    order = ["Burger", "Coffee", "Pizza"]
    total_cost = restaurant.calculate_total_cost(order)
    print(f"Total cost of the order: ${total_cost:.2f}")
