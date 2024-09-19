# Import required libraries and modules
import os
from dictionary import food_menu, drinks_menu, book_collection, customers, Customer_Order_Preference
from specials import get_day_of_week, display_introduction

# Name of the Book Cafe
book_shop = 'pythoneers'

# List that will contain customer orders
order = []

def main_menu():
    print(f"📚 Welcome to the {book_shop.title()} Book Cafe! ☕\n")
    print("📋 Here are your options:")
    print("1️⃣  See Food and Drinks Menu")
    print("2️⃣  Best-Selling Book Collection")
    print("3️⃣  View Today's Specials")
    print("4️⃣  Employee Section")
    print("5️⃣  View Your Order 🧾")
    print("6️⃣  Submit Order ✅")
    print("7️⃣  Exit 🚪")

    choice = int(input("\nWhat would you like today? (1-7): "))

    if choice == 1:
        clear_console()
        food_drinks_menu()
    elif choice == 2:
        clear_console()
        view_book_collection()
        order_input(book_collection)
    elif choice == 3:
        clear_console()
        display_introduction()
    elif choice == 4:
        clear_console()
        employee_menu()
    elif choice == 5:
        view_order()
        view_total()
    elif choice == 6:
        clear_console()
        finalize_order()
    else:
        print("Thank you for visiting! 😊")
        exit()

def order_input(menu_dict):
    while True:
        selection = input("\nPlease type a selection (enter 'done' to exit): ")
        if menu_dict.get(selection):
            print(f"✅ {selection} has been added to your order.")
            order.append([selection, menu_dict[selection]])
        elif selection.lower() == "done":
            clear_console()
            main_menu()
            break
        else:
            print("⚠️ Invalid selection, please try again.")

def view_food_menu():
    print("🍽️ Food Menu:")
    for food, price in food_menu.items():
        print(f"-- {food} £{price}" )

def view_drinks_menu():
    print("🥤 Drinks Menu:")
    for drink, price in drinks_menu.items():
        print(f"-- {drink} £{price}" )

def view_book_collection():
    print("📚 Book Collection:")
    for book, price in book_collection.items():
        print(f"-- {book} £{price}")
    print("\nRemember: Books are free with a book pass! 🎟️")

def food_drinks_menu():
    print("\nWould you like the Food or Drinks Menu:")
    print("1️⃣  Food Menu 🍽️")
    print("2️⃣  Drinks Menu 🥤")
    print("3️⃣  View Your Order 🧾")
    print("4️⃣  Go Back to Main Menu 🔙")

    choice = int(input("\nInput choice here: "))

    if choice == 1:
        clear_console()
        view_food_menu()
        order_input(food_menu)
    elif choice == 2:
        clear_console()
        view_drinks_menu()
        order_input(drinks_menu)
    elif choice == 3:
        view_order()
        view_total()
        food_drinks_menu()
    elif choice == 4:
        clear_console()
        main_menu()

def employee_menu():
    print("👩‍💼 Employee Section:")
    print("1️⃣  Update Book Pricing")
    print("2️⃣  Get Customer Info 🧑‍💼")
    print("3️⃣  Go Back to Main Menu 🔙")

    choice = int(input("\nInput choice here: "))

    if choice == 1:
        update_book(input("Book name: "), input("Insert new price: "))
    elif choice == 2:
        clear_console()
        get_customer_info()
    elif choice == 3:
        clear_console()
        main_menu()

def update_book(name, price):
    if book_collection.get(name):
        book_collection[name] = price
        print(f"📖 {name} price has been updated to £{book_collection[name]}")
    else:
        print("⚠️ Invalid selection, please try again.")

def print_customer_info(name, address, preferences):
    print(f"👤 Customer Name: {name}")
    print(f"🏠 Address: {address}")
    print("🍽️ Favorite Order:")
    print(f"  Food: {preferences['Food']}")
    print(f"  Drink: {preferences['Drink']}")
    print(f"  Book: {preferences['Book']}")
    print()

def get_customer_info():
    name = input("Enter customer name: ").strip()
    address = customers.get(name)
    preferences = Customer_Order_Preference.get(name, {
        "Food": "No preference",
        "Drink": "No preference",
        "Book": "No preference"
    })

    if address:
        print_customer_info(name, address, preferences)
    else:
        print("⚠️ Customer not found.")

def view_order():
    clear_console()
    print("🧾 Customer Order:")
    for item in order:
        print(item)
    print()

def clear_console():
    os.system("cls" if os.name == "nt" else "clear")

def finalize_order():
    view_order()
    view_total()

    print("Choose an option:")
    print("1️⃣  Submit Order ✅")
    print("2️⃣  Clear Order 🗑️")
    print("3️⃣  Go Back 🔙")

    choice = int(input("--> "))

    if choice == 1:
        clear_console()
        submit_order()
    elif choice == 2:
        clear_console()
        order.clear()
        finalize_order()
    elif choice == 3:
        clear_console()
        main_menu()

def submit_order():
    view_order()
    print("Choose an option:")
    print("1️⃣  Order as Guest 👤")
    print("2️⃣  Returning Customer 💼")
    print("3️⃣  Cancel ❌")

    choice = int(input("--> "))

    if choice == 1:
        new_cust_name = input("Enter your name: ").title()
        new_cust_addr = input("Enter your address: ")
        order_sent(new_cust_name, new_cust_addr)
    elif choice == 2:
        clear_console()
        returning_customer()
    elif choice == 3:
        clear_console()
        main_menu()

def view_total():
    total = 0.00
    for item, price in order:
        total += float(price)
    print(f"💰 Final Total: £{total:.2f}\n")

def order_sent(name, address):
    view_order()
    view_total()

    print(f"📦 Order confirmed for {name}.")
    print(f"📍 To be delivered to: {address}")
    print("\nThank you for your order! 😊")
    order.clear()

def returning_customer():
    view_order()
    view_total()

    cust_name = input("Enter your full name: ").title()

    if customers.get(cust_name):
        print(f"Account found. Please confirm address: {customers[cust_name]}")
        confirm = input("Confirm Y/n: ")

        if confirm.upper() == "Y":
            order_sent(cust_name, customers[cust_name])
        else:
            clear_console()
            returning_customer()
    else:
        print("⚠️ Account not found, please try again.")
        clear_console()
        returning_customer()

# Start the app
clear_console()
while True:
    main_menu()
