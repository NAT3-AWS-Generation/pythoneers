

book_shop = 'pythoneers'

#this is where the program starts

def main_menu():

    print(f'Welcome to the {book_shop.title()} book cafe!\n')

    print('instruction')

    print()

    print('1.Select to see food and drinks menu')
    print('2.Select for best-selling book collection')
    print('3.Employee section')
    print('4.View order')
    print('5.Exit')

    choice = input()

    if choice == 1:
        food_drinks_menu()
    elif choice == 2:
        book_menu()
    elif choice == 3:
        employee_menu()
    elif choice == 5:
        print('exit program')


main_menu()

def food_drinks_menu():
    
    print('Select food or drink')

    print('1.Food')
    print('2.Drink')
    print('3.View order')
    print('4.Go back to main menu')

    choice = input('input choice here:')
    
    if choice == 1:
        food_menu()
    elif choice == 2:
        drinks_menu()
    elif choice == 3:
        view_order()
    elif choice == 4:
        main_menu()
    
    




def book_menu():
    pass

def employee_menu():
    pass

def view_order():
    pass


