from abc import ABC, abstractmethod
from exceptions import MenuItemNotFoundException

class MenuItem(ABC):
    def __init__(self, name, price):
        self.name = name
        self.price = price

    @abstractmethod
    def __str__(self):
        pass

class Food(MenuItem):
    def __init__(self, name, price, description):
        super().__init__(name, price)
        self.description = description

    def __str__(self):
        return f"{self.name} - {self.price:.2f} ({self.description})"

class Drink(MenuItem):
    def __init__(self, name, price, description):
        super().__init__(name, price)
        self.description = description

    def __str__(self):
        return f"{self.name} - {self.price:.2f} ({self.description})"

class Menu:
    def __init__(self):
        self.menu_items = []

    def add_item(self, menu_item: MenuItem):
        self.menu_items.append(menu_item)

    def remove_item(self, name: str):
        for item in self.menu_items:
            if item.name == name:
                self.menu_items.remove(item)
                return
        raise MenuItemNotFoundException(f"Menu item '{name}' not found.")

    def display_menu(self):
        print("Menu:")
        for item in self.menu_items:
            print(item)

    def get_item_by_name(self, name: str) -> MenuItem:
        for item in self.menu_items:
            if item.name == name:
                return item
        raise MenuItemNotFoundException(f"Menu item '{name}' not found.")
