##pseudo-code

##Basic Pseudo-code

'''initialize Application'''
LOAD menu_items (food, drinks)
LOAD book_list
LOAD customer_data (if any)

'''main menu'''
WHILE True
    DISPLAY "1. Customer"
    DISPLAY "2. Employee"
    DISPLAY "3. Exit"
    GET user_choice

    IF user_choice == 1 THEN
        // Customer Options
        DISPLAY "1. View Menu and Books"
        DISPLAY "2. Order Items"
        DISPLAY "3. Exit"
        GET customer_choice

        IF customer_choice == 1 THEN
            DISPLAY food_and_drink_menu
            DISPLAY book_list

        ELSE IF customer_choice == 2 THEN
            DISPLAY "Choose food and drinks:"
            GET food_and_drink_choices
            DISPLAY "Choose books:"
            GET book_choices
            COLLECT customer_details
            CONFIRM and SAVE order

        ELSE IF customer_choice == 3 THEN
            CONTINUE // Go back to Main Menu

        ELSE
            DISPLAY "Invalid choice."

    ELSE IF user_choice == 2 THEN
        // Employee Options
        DISPLAY "1. Update Menu and Books"
        DISPLAY "2. Update Specials"
        DISPLAY "3. View Orders"
        DISPLAY "4. Exit"
        GET employee_choice

        IF employee_choice == 1 THEN
            DISPLAY "Update Menu and Books"
            // Add, Update, or Remove items

        ELSE IF employee_choice == 2 THEN
            DISPLAY "Update Specials"
            // Add, Update, or Remove specials

        ELSE IF employee_choice == 3 THEN
            DISPLAY "View Orders"
            // Display orders and customer details

        ELSE IF employee_choice == 4 THEN
            CONTINUE // Go back to Main Menu

        ELSE
            DISPLAY "Invalid choice."

    ELSE IF user_choice == 3 THEN
        // Save changes and Exit
        DISPLAY "Goodbye!"
        BREAK // Exit the loop

    ELSE
        DISPLAY "Invalid choice."
END WHILE
