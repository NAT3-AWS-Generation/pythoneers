food_menu = {
    "Croissant": "2.50",
    "Sandwich of the Day": "4.00",  # This changes every day
    "Cake of the Day": "3.00",  # This changes every day
    "Bagel": "2.80",
    "Muffin": "2.20",
    "Pasta Salad": "5.00",
    "Quiche": "4.50",
    "Soup of the Day": "3.80"
}
 
drinks_menu = {
    "Coffee": "2.00",
    "Tea": "1.50",
    "Smoothie": "3.50",
    "Hot Chocolate": "2.80",
    "Latte": "2.50",
    "Espresso": "1.80",
    "Iced Coffee": "3.00",
    "Orange Juice": "2.50"
}
 
book_collection = {  
"The Great Gatsby": "1.00",  
"1984": "1.50",
"To Kill a Mockingbird":"1.00",  
"Pride and Prejudice": "2.00",  
"Moby Dick": "1.00",  
"The Catcher in the Rye": "1.50",    
"Brave New World": "1.00",
"The Hobbit": "1.00" }
# We can make a comment saying if you have a book pass. Books are free
 
# Daily specials
daily_sandwiches = {
    "Monday": "Turkey Sandwich",
    "Tuesday": "Ham & Cheese Sandwich",
    "Wednesday": "Chicken Salad Sandwich",
    "Thursday": "Tuna Melt Sandwich",
    "Friday": "BLT Sandwich",
    "Saturday": "Veggie Wrap",
    "Sunday": "Club Sandwich"
}
 
daily_cakes = {
    "Monday": "Chocolate Cake",
    "Tuesday": "Cheesecake",
    "Wednesday": "Carrot Cake",
    "Thursday": "Lemon Drizzle Cake",
    "Friday": "Red Velvet Cake",
    "Saturday": "Victoria Sponge",
    "Sunday": "Apple Pie"
}

def view_food_menu():
    print("Food Menu:")
    for food, price in food_menu.items():
        print(f"-- {food} £{price}" )


def view_drinks_menu():
    print("Drinks Menu:")
    for drink, price in drinks_menu.items():
        print(f"-- {drink} £{price}" )

def view_book_collection():
    print("Book Selection")
    for book, price in book_collection.items():
        print(f"-- {book} £{price}")

    print("\n Books are free with book pass.")


def order_input(menu_dict):
    while True:
        selection = input("Please type a selection (enter 'done' to exit): ")
        if menu_dict.get(selection):
            print(f"{selection} has been added to your order")
        elif selection.lower() == "done":
            break
        else:
            print("Invalid selection, please try again.")
    