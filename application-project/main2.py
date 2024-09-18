

book_shop = 'pythoneers'

#this is the dictionaires

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

#this is where the program starts



order = []

def main_menu():

    print(f'Welcome to the {book_shop.title()} book cafe!\n')

    print('instruction')

    print()

    print('1.Select to see food and drinks menu')
    print('2.Select for best-selling book collection')
    print('3.Employee section')
    print('4.View order')
    print('5.Exit')

    choice = input('What would you like today:')

    if choice == 1:
        print('hello')
        food_drinks_menu()
    elif choice == 2:
        book_menu()
    elif choice == 3:
        employee_menu()
    elif choice == 5:
        print('exit program')



def food_drinks_menu():
    
    print('Select food or drink:')

    print('1.Food')
    print('2.Drink')
    print('3.View order')
    print('4.Go back to main menu')

    choice = input('Input choice here:')
    
    if choice == 1:
        view_food_menu()
        order_input(food_menu)
    elif choice == 2:
        drinks_menu()
    elif choice == 3:
        view_order()
    elif choice == 4:
        main_menu()


def order_input(menu_dict):
    while True:
        selection = input("Please type a selection (enter 'done' to exit): ")
        if menu_dict.get(selection):
            print(f"{selection} has been added to your order")
        elif selection.lower() == "done":
            break
        else:
            print("Invalid selection, please try again.")
    


def view_food_menu():
    print("Food Menu:")
    for food, price in food_menu.items():
        print(f"-- {food} £{price}" )  

def food_menu():

    print('Select your choice of food')

    print('1.')
    print('2.')
    print('.View order')
    print('.Go back to main menu')

    choice = input('Input choice here:')

    if choice == 1:
        pass
    elif choice == 2:
        pass
    elif choice == 3:
        pass
    elif choice == 4:
        main_menu()
    
def drinks_menu():

    print('Select your choice of drink')

    print('1.')
    print('2.')
    print('.View order')
    print('.Go back to main menu')

    choice = input('Input choice here:')

    if choice == 1:
        pass
    elif choice == 2:
        pass
    elif choice == 3:
        pass
    elif choice == 4:
        main_menu()
    
   

def book_menu():
    
    print('Select your book of choice')

    print('1.')
    print('2.')
    print('.View order')
    print('.Go back to main menu')

    choice = input('Input choice here:')

    if choice == 1:
        pass
    elif choice == 2:
        pass
    elif choice == 3:
        pass
    elif choice == 4:
        main_menu()



def employee_menu():
    
    print('Select what you would like to update')

    print('1.Update book')
    print('2.Update special')
    print('3.Get customer info')
    print('4.Go back to main menu')

    choice = input('Input choice here:')



def view_order():
    
    print('Customer order:')


main_menu()