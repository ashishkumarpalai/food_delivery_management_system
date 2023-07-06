from tabulate import tabulate

menu = [
    {"id": 1, "name": "Pizza", "price": 10.99, "availability": True},
    {"id": 2, "name": "Burger", "price": 5.99, "availability": True},
    {"id": 3, "name": "Pasta", "price": 8.99, "availability": False},
]

orders = []

def find_dish_by_id(dish_id):
    for dish in menu:
        if dish["id"] == dish_id:
            return dish
    return None

def find_order_by_id(order_id):
    for order in orders:
        if order["id"] == order_id:
            return order
    return None

def print_menu():
    headers = ["ID", "Dish Name", "Price", "Availability"]
    table_data = []

    for dish in menu:
        availability = "Available" if dish["availability"] else "Unavailable"
        table_data.append([dish["id"], dish["name"], dish["price"], availability])

    print("==== Zesty Zomato Menu ====")
    print(tabulate(table_data, headers=headers, tablefmt="grid"))

def add_dish():
    dish_id = int(input("Enter the dish ID: "))
    dish_name = input("Enter the dish name: ")
    price = float(input("Enter the price: "))
    availability = True if input("Is the dish available? (yes/no): ").lower() == "yes" else False

    dish = {"id": dish_id, "name": dish_name, "price": price, "availability": availability}
    menu.append(dish)
    print("Dish added successfully!")

def remove_dish():
    dish_id = int(input("Enter the dish ID to remove: "))
    for dish in menu:
        if dish["id"] == dish_id:
            menu.remove(dish)
            print("Dish removed successfully!")
            break
    else:
        print("Dish not found!")

def update_dish_availability():
    dish_id = int(input("Enter the dish ID to update availability: "))
    for dish in menu:
        if dish["id"] == dish_id:
            availability = True if input("Is the dish available now? (yes/no): ").lower() == "yes" else False
            dish["availability"] = availability
            print("Availability updated successfully!")
            break
    else:
        print("Dish not found!")

def take_order():
    customer_name = input("Enter customer name: ")
    order_items = []
    total_price = 0  # Initialize total price variable
    while True:
        dish_id = int(input("Enter dish ID (0 to finish): "))
        if dish_id == 0:
            break
        dish = find_dish_by_id(dish_id)
        if dish is None:
            print("Invalid dish ID!")
        elif not dish["availability"]:
            print("This dish is currently unavailable!")
        else:
            order_items.append(dish)
            total_price += dish["price"]  # Add dish price to total price
    if order_items:
        order_id = len(orders) + 1
        order = {"id": order_id, "customer_name": customer_name, "items": order_items, "status": "received"}

        # Add total items and total price to the order
        order["total_items"] = len(order_items)
        order["total_price"] = total_price

        orders.append(order)
        print("Order placed successfully!")


def update_order_status():
    order_id = int(input("Enter the order ID to update status: "))
    order = find_order_by_id(order_id)
    if order is not None:
        new_status = input("Enter the new status: ")
        order["status"] = new_status
        print("Order status updated successfully!")
    else:
        print("Order not found!")


def print_orders():
    headers = ["Order ID", "Customer Name", "Items", "Total Items", "Total Price", "Status"]
    table_data = []

    for order in orders:
        order_id = order["id"]
        customer_name = order["customer_name"]
        items = ", ".join(item["name"] for item in order["items"])
        total_items = order["total_items"]
        total_price = order["total_price"]
        status = order["status"]
        table_data.append([order_id, customer_name, items, total_items, total_price, status])

    print("==== Zesty Zomato Orders ====")
    print(tabulate(table_data, headers=headers, tablefmt="grid"))


def print_menu():
    headers = ["ID", "Dish Name", "Price", "Availability"]
    table_data = []

    for dish in menu:
        availability = "Available" if dish["availability"] else "Unavailable"
        table_data.append([dish["id"], dish["name"], dish["price"], availability])

    print("==== Zesty Zomato Menu ====")
    print(tabulate(table_data, headers=headers, tablefmt="grid"))

def main():
    while True:
        print("==== Zesty Zomato Management System ====")
        print("1. Show all menu items")
        print("2. Add a dish to the menu")
        print("3. Remove a dish from the menu")
        print("4. Update dish availability")
        print("5. Take a new order")
        print("6. Update order status")
        print("7. Review all orders")
        print("8. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            print_menu()
        elif choice == "2":
            add_dish()
        elif choice == "3":
            remove_dish()
        elif choice == "4":
            update_dish_availability()
        elif choice == "5":
            take_order()
        elif choice == "6":
            update_order_status()
        elif choice == "7":
            print_orders()
        elif choice == "8":
            print("Exiting...")
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()