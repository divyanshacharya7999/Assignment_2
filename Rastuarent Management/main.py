from restaurant import Restaurant
from menu import Food, Drink

def main():
    restaurant = Restaurant()
    restaurant.add_menu_item(Food("Pizza", 200, "Onion Pizza"))
    restaurant.add_menu_item(Drink("Cola", 60, "Coca-Cola"))
    restaurant.add_menu_item(Drink("Wine", 500, "Budweiser"))

    order = restaurant.place_order()

    print("\nOrder Summary:")
    order.display_order()
    total_cost = order.calculate_total()
    print(f"Total cost of the order: {total_cost:.2f}")

if __name__ == "__main__":
    main()
