import os

def order_input(menu_dict):
    while True:
        selection = input("\nPlease type a selection (enter 'done' to exit): ")
        if menu_dict.get(selection):
            print(f"\n{selection} has been added to your order")
            order.append([selection, menu_dict[selection]])
        elif selection.lower() == "done":
            clear_console()
            main_menu()
            break
        else:
            print("\nInvalid selection, please try again.")

def view_food_menu():
    print("\nFood Menu:")
    for food, price in food_menu.items():
        print(f"-- {food} £{price}" )

def view_drinks_menu():
    print("\nDrinks Menu:")
    for drink, price in drinks_menu.items():
        print(f"-- {drink} £{price}" )

def view_book_collection():
    print("\nBook Selection")
    for book, price in book_collection.items():
        print(f"-- {book} £{price}")

    print("\nRemember: Books are free with book pass.")

def food_drinks_menu():
    print("\n Would you like the Food or Drinks menu:")

    print("1. Food")
    print("2. Drink")
    print("3. View order")
    print("4. Go back to main menu")

    choice = int(input("\nInput choice here:"))
    
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
    print("\nSelect what you would like to update")

    print("1. Update book")
    print("2. Get customer info")
    print("3. Go back to main menu")

    choice = int(input("\nInput choice here:"))

    if choice == 1:
        update_book( input("Book name: "), input("Insert new price: "))
    elif choice == 2:
        clear_console()
        get_customer_info()
    elif choice == 3:
        clear_console()
        main_menu()

def update_book(name, price):
    if book_collection.get(name):
        book_collection[name] = price
        print(name, "price has been updated to £", book_collection[name])
        print()
    else:
        print("Invalid selection, please try again")

# Function to print customer info
def print_customer_info(name, address, preferences):
    """Print formatted customer information."""
    print(f"Customer Name: {name}")
    print(f"Address: {address}")
    print("Favorite Order:")
    print(f"  Food: {preferences['Food']}")
    print(f"  Drink: {preferences['Drink']}")
    print(f"  Book: {preferences['Book']}")
    print()

def get_customer_info():
    """Retrieve and display customer information based on their name."""
    name = input("Enter customer name to retrieve information: ").strip()
    
    # Retrieve address and preferences from dictionaries
    address = customers.get(name)
    preferences = Customer_Order_Preference.get(name, {
        "Food": "No preference",
        "Drink": "No preference",
        "Book": "No preference"
    })
    
    if address:
        print_customer_info(name, address, preferences)
    else:
        print("Customer not found.")

def view_order():
    clear_console()
    print("\nCustomer order:")
    for item in order:
        print(item)
    print()

# This clears the console
def clear_console():
    os.system("cls")

def finalize_order():
    view_order()
    view_total()

    print("Choose an option:")
    print("1. Submit Order")
    print("2. Clear order")
    print("3. Go back.")

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

    print("Choose an option")
    print("1. Order as guest.")
    print("2. Returning Customer")
    print("3. Cancel")

    choice = int(input("-->"))

    if choice == 1:
        new_cust_name = input("Please enter your full name: ").title()
        new_cust_addr = input("Please enter your full address: ")
        order_sent(new_cust_name, new_cust_addr)
        print()
        main_menu()
    elif choice == 2:
        clear_console()
        returning_customer()
    elif choice == 3:
        clear_console()
        main_menu()

def view_total():
    total : float = 0.00
    for n, i in order:
        total += float(i)

    print("Final Total: £", sep="",  end="")
    print("{:.2f}".format(total))
    print()
        
def order_sent(name, address):
    view_order()
    view_total()

    print("The order listed above has been confirmed:")
    print(f"To {name} at the following address:")
    print(address)
    print("\nThank you for your order. :)\n")
    order.clear()

def returning_customer():
    view_order()
    view_total()
    cst_search = input("Please enter your full name: ").title()
    if customers.get(cst_search):
        print("Account found, please confirm your address:")
        print(customers[cst_search])
        confirm = input("Confirm Y/n: ")
        if confirm.upper() == "Y":
            order_sent(cst_search, customers[cst_search])
        else:
            clear_console()
            returning_customer()
    else:
        print("Account not found, please try again.")
        clear_console()
        returning_customer()