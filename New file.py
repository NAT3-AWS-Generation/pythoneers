# Define the dictionaries
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
    "To Kill a Mockingbird": "1.00",  
    "Pride and Prejudice": "2.00",  
    "Moby Dick": "1.00",  
    "The Catcher in the Rye": "1.50",    
    "Brave New World": "1.00",
    "The Hobbit": "1.00"
}

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

customers = {
    "Jaqueline Sharp": "123 Passenger Drive",
    "Peter Greene": "24 Hillside Ave",
    "Freddie Flintoff": "29 Blackview Rd",
    "Mohammed Hijab": "1 Herring Rd",
    "Adonis Creed": "64 Cobble Street",
    "Suzy Blackham": "52 Downham Rd"
}

Customer_Order_Preference = {
    "Jaqueline Sharp": {
        "Food": "Croissant",
        "Drink": "Coffee",
        "Book": "The Great Gatsby"
    },
    "Peter Greene": {
        "Food": "Sandwich of the Day",
        "Drink": "Latte",
        "Book": "1984"
    },
    "Freddie Flintoff": {
        "Food": "Muffin",
        "Drink": "Smoothie",
        "Book": "To Kill a Mockingbird"
    },
    "Mohammed Hijab": {
        "Food": "Pasta Salad",
        "Drink": "Iced Coffee",
        "Book": "Pride and Prejudice"
    },
    "Adonis Creed": {
        "Food": "Bagel",
        "Drink": "Latte",
        "Book": "Moby Dick"
    },
    "Suzy Blackham": {
        "Food": "Quiche",
        "Drink": "Tea",
        "Book": "The Catcher in the Rye"
    }
}

# Function to print customer info
def print_customer_info(name, address, preferences):
    """Print formatted customer information."""
    print(f"Customer Name: {name}")
    print(f"Address: {address}")
    print("Favorite Order:")
    print(f"  Food: {preferences['Food']}")
    print(f"  Drink: {preferences['Drink']}")
    print(f"  Book: {preferences['Book']}")

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

# Example usage of the functions (replace this with actual program flow)
if __name__ == "__main__":
    get_customer_info()