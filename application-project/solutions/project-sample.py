# Initialize the data
menu_items = {
    'food': ['sandwich', 'cake', 'coffee', 'tea'],
    'drinks': ['coffee', 'tea', 'juice']
}
book_list = ['The Great Gatsby', '1984', 'To Kill a Mockingbird']

customer_data = {}  # This can be used to store customer details if needed

def display_menu_and_books():
    print("Food Menu:", menu_items['food'])
    print("Drink Menu:", menu_items['drinks'])
    print("Books Available:", book_list)

def collect_order():
    print("Choose food and drinks (separate choices by commas):")
    food_choices = input().split(',')
    print("Choose books (separate choices by commas):")
    book_choices = input().split(',')
    print("Enter your name:")
    customer_name = input()
    print("Enter your address:")
    customer_address = input()
    
    customer_data[customer_name] = {
        'address': customer_address,
        'food': food_choices,
        'books': book_choices
    }
    
    print("Order confirmed!")
    print(f"Name: {customer_name}, Address: {customer_address}")
    print("Food ordered:", food_choices)
    print("Books ordered:", book_choices)

def update_menu_and_books():
    print("Update Menu and Books:")
    print("1. Add food item")
    print("2. Remove food item")
    print("3. Add drink item")
    print("4. Remove drink item")
    print("5. Add book")
    print("6. Remove book")
    choice = input("Select an option: ")
    
    if choice == '1':
        item = input("Enter food item to add: ")
        menu_items['food'].append(item)
    elif choice == '2':
        item = input("Enter food item to remove: ")
        menu_items['food'].remove(item)
    elif choice == '3':
        item = input("Enter drink item to add: ")
        menu_items['drinks'].append(item)
    elif choice == '4':
        item = input("Enter drink item to remove: ")
        menu_items['drinks'].remove(item)
    elif choice == '5':
        item = input("Enter book to add: ")
        book_list.append(item)
    elif choice == '6':
        item = input("Enter book to remove: ")
        book_list.remove(item)
    else:
        print("Invalid choice.")

def view_orders():
    print("Customer Orders:")
    for customer, details in customer_data.items():
        print(f"Name: {customer}")
        print(f"Address: {details['address']}")
        print(f"Food: {details['food']}")
        print(f"Books: {details['books']}")
        print()

# Main loop
while True:
    print("\nMenu:")
    print("1. Customer")
    print("2. Employee")
    print("3. Exit")
    user_choice = input("Select an option: ")

    if user_choice == '1':
        print("Customer Options:")
        print("1. View Menu and Books")
        print("2. Order Items")
        print("3. Exit")
        customer_choice = input("Select an option: ")

        if customer_choice == '1':
            display_menu_and_books()
        elif customer_choice == '2':
            collect_order()
        elif customer_choice == '3':
            continue  # Go back to Main Menu
        else:
            print("Invalid choice.")

    elif user_choice == '2':
        print("Employee Options:")
        print("1. Update Menu and Books")
        print("2. View Orders")
        print("3. Exit")
        employee_choice = input("Select an option: ")

        if employee_choice == '1':
            update_menu_and_books()
        elif employee_choice == '2':
            view_orders()
        elif employee_choice == '3':
            continue  # Go back to Main Menu
        else:
            print("Invalid choice.")

    elif user_choice == '3':
        print("Goodbye!")
        break  # Exit the loop

    else:
        print("Invalid choice.")
