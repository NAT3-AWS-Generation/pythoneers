from datetime import datetime
from dictionary import daily_sandwiches, daily_cakes, book_collection

# Helper function to get the current day
def get_day_of_week():
    return datetime.now().strftime('%A')
 
# Function to display the daily specials and introduction
def display_introduction():
    """Display the introduction with daily specials and favorite books."""
    current_day = get_day_of_week()
    sandwich_of_the_day = daily_sandwiches.get(current_day, "Not available today")
    cake_of_the_day = daily_cakes.get(current_day, "Not available today")
   
    print("Welcome to the Pythoneers Bookshop and Cafe!")
    print(f"Today is {current_day}!")
    print(f"Today's Sandwich of the Day is: {sandwich_of_the_day}")
    print(f"Today's Cake of the Day is: {cake_of_the_day}\n")
   
    print("Check out our drinks menu and favorite books for today!\n")
   
    print("Today's favorite books:")
    for book, price in book_collection.items():
        print(f"- {book}: £{price}")
   
    print("\nRemember to bring your Book Pass to take your favorite book home with you!\n")