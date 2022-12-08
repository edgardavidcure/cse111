from datetime import datetime
import random

#Store Departments used to identify the dictionaries with items and prices
departments = ["groceries", "appliances", "furniture"]
order_numbers = [ 3248549, 4358344, 4987934, 8783473, 8947359, 4353478, 9089585, 1238392]

#Groceries dictionary with items and prices included
groceries = {
    "bread" : 3.90,
    "egg": 0.80,
    "milk" : 4.99,
    "apple" : 2.19,
    "banana" : 1.49
}

#Appliances dictionary with items and prices included
appliances = {
    "microwave" : 199.99, 
    "fridge" : 1399.99, 
    "oven" : 799.99, 
    "blender" : 89.99, 
    "tv" : 1099.99

}

#Furniture dictionary with items and prices included
furniture = {
    "couch" : 1899.99, 
    "desk" : 499.99, 
    "chair" : 129.99, 
    "bed" : 899.99, 
    "carpet" : 139.99
}




#List of actions available in our program for each department. Inlcuded on a list to be able to use its individual indexes and print individually

list_of_actions = [ "view items", "add items", "view cart", "remove items", "compute total", "quit", "change department", "print receipt"]

#Indexes for each action specified with and added number to start from index #1 
view_items = list_of_actions.index("view items") + 1
add_items = list_of_actions.index("add items") + 1
view_cart_total = list_of_actions.index("view cart") + 1
remove_items = list_of_actions.index("remove items") + 1
compute_total = list_of_actions.index("compute total")+ 1
quit = list_of_actions.index("quit")+ 1
change_department = list_of_actions.index("change department")+ 1
print_receipt = list_of_actions.index("print receipt")+ 1

#Empty lists created to store prices and items added to the cart
cart = []
cart_prices = []

#Main function. All errors are specified to be handled. Multiple while loops are created to allow the program to keep running after user specifies desired actions. 
def main():
    try:
        act = True
        print()
        print ("Welcome to BestBy!\n")
        #This conditions for the loop allow the program to run from this point if the user wants to change departments or if the program is barely started 
        while act != quit or act == change_department:
            #This conditional works if the user has opted to change the department at any point, and sets the variable act as True, to be able to meet the conditions for all the other while loops below. It basically sets the variable to its original value.
            if act == change_department:
                act = True
            print (f"Our store has different departments where you can find what you need.\nHere they are: ")
            print()
        
            display_departments()
            print()
            input_ = int(input("Enter desired department number: "))
            #This condition handles an error where users could select a greater or lower number of departments
            if input_ > len(departments) or input_ <= 0:
                print()
                print("Department Not Found. Enter The Right Number")
                print()
                act = change_department
            else: 
                #If there is no error, the right department will be found
                department_input = select_department(input_)
            
            while act != change_department:
                if department_input in departments:
                    if department_input == "groceries":
                        def get_dict(groceries):
                            return groceries
                        department = get_dict(groceries)
                    elif department_input == "appliances":
                        def get_dict(appliances):
                            return appliances
                        department = get_dict(appliances)
                    elif department_input == "furniture":
                        def get_dict(furniture):
                            return furniture
                        department = get_dict(furniture)
                    print()
                    if act == True:
                        print (f"Welcome to our {department_input} department\n")
                    elif act != True:
                        act = quit
                        break
                    
                    while act != quit:
                        display_actions()

                        print()
                        act = int(input ("What would you like to do? "))
                        if act == view_items:
                            display_items(department_input)
                        elif act == add_items:
                            display_items(department_input)
                            department_prices = get_prices(department)
                            add_input = int(input("What item would you like to add? "))
                            
                            
                            for number, (article, price) in enumerate(zip(department, department_prices), start=1 ):
                                
                                if add_input == number:
                                    add_items_to_cart(add_input, article, department)
                            #This condition handles an error where the item number entered by the user is greater or lower than the items available
                            if add_input > number or add_input <= 0:
                                print("Item Not Found. Enter The Right Number")
                                act = True
                                break
                        elif act == view_cart_total:
                            if len(cart) == 0:
                                print("There are not items in the cart yet. Make sure you add something first.")
                                act = True
                                break
                            else:
                                view_cart()
                        elif act == remove_items:
                            #this condition handles an error where the user wants to remove items from the cart before adding any. 
                            if len(cart) == 0:
                                print("There are not items in the cart yet. Make sure you add something first.")
                                act = True
                                break
                            else:
                                view_cart()
                                remove = int(input("What items would you like to remove? Please enter the number of the item: "))
                                if remove > number:
                                    print("Sorry, that item number is not in the cart.")
                                else:
                                    print (f"The item has been removed.")
                                    remove_cart_items(remove)
                                    view_cart()
                                
                        elif act == compute_total:
                            view_cart()
                            total = compute_total_cart()
                            print(f"The total in your shopping cart is: ${total:.2f}")
                        elif act == quit:
                            print ("Thank you for shopping at BestBy, see you next time!")
                            print()
                            break
                        elif act == change_department:
                            break
                        elif act == print_receipt:
                            get_receipt()
                            act = quit
                        #This condition handles an error where the user enters a number greater than the possible actions available
                        elif act > print_receipt:
                            print("You entered a wrong number. Please try again.")
                            act = True
                            break
    except ZeroDivisionError as zero_div_err:
        print(zero_div_err)
        
    except TypeError as type_err:
        print(type_err)
        
    except ValueError as val_err:
        print(val_err)
        print("Please enter a number next time. Integers are not accepted.")
    except IndexError as index_err:
        print(index_err)
        
    except KeyError as key_err:
        print(type(key_err).__name__, key_err)
        



                        
                    

#Function created to get a random order number from the order numbers lists at the beginning of the program. Takes no parameters.
def get_order_number():
    order_number = random.choice(order_numbers)
    return order_number


#Function created to print a receipt that gets the current date and time, the name of the store, the order number, items in the cart, subtotal and total with taxes
def get_receipt():
    print()
    print()
    date = datetime.now()
    print(f"{date:%a %b %d %I:%M %p %Y }")
    print()
    print("BestBy - Los Angeles, CA")
    print()
    print(f"Your order number is: {get_order_number()}")
    print()
    view_cart()
    print()
    subtotal = compute_total_cart()
    print(f"Subtotal = ${subtotal:.2f}")
    tax = subtotal * 0.08
    print(f"Sales Tax = ${tax:.2f}")
    total = subtotal + tax
    print()
    print(f"Total = ${total:.2f}")
    print()
    print("Thanks for shopping at BestBy today. See you next time!")
    
#Function created to show a lists of departments available in the store. Takes no parameters. 
# A for loop iterates through the departments lists at 
# the beginning of the program and enumerates the departments 
# with numbers that start counting from 1.
def display_departments():
    for number, department in enumerate(departments, start=1):
        print (f"{number}. {department.capitalize()}")
    
#Function created to convert the department string to a index number that allows the user to 
# get the department he wants to shop at. The function takes a number as a parameter where the user inputs the number the department they want, 
# and the for loop iterates through the list of departments, the conditional verifies that the input matches the number of the department desired 
# and then returns the desired department
def select_department(input_):
    for number, department in enumerate(departments, start=1):
        if input_ == number:
            department_number = number
            desired_department = department

    return desired_department

#Function created to print the actions available with an index number that starts at 1
def display_actions():
    print ("Here is a list of actions you can take:\n")
    for number, action in enumerate(list_of_actions, start = 1):
        print (f"{number}. {action.capitalize()}")                  
    print()
#Function created to get the prices for the items in the department. The conditionals find the dictionary needed 
# to process its keys and values. It takes a department name as a parameter.
def get_prices(department):    
    department_prices = []
    if department == "groceries":
        def get_dict(groceries):
            return groceries
        department = get_dict(groceries)
    elif department == "appliances":
        def get_dict(appliances):
            return appliances
        department = get_dict(appliances)
    elif department == "furniture":
        def get_dict(furniture):
            return furniture
        department = get_dict(furniture)

    for article in list(department):
        price = department[article]
        department_prices.append(price)
    return department_prices

#Function created to display the items in the department. The conditionals find the dictionary needed 
# to process its keys and values. It takes a department name as a parameter.
def display_items(department):
    print (f"Here is a list of the items available in our {department} department: ")
    print()

    if department == "groceries":
        def get_dict(groceries):
            return groceries
        department = get_dict(groceries)
    elif department == "appliances":
        def get_dict(appliances):
            return appliances
        department = get_dict(appliances)
    elif department == "furniture":
        def get_dict(furniture):
            return furniture
        department = get_dict(furniture)
    

    department_prices = get_prices(department)
    for number, (article, price) in enumerate(zip(department, department_prices), start=1 ):
            print (f"{number}. {article.capitalize()} - ${price:.2f}")
    print()

#Function created to add the items desired to the cart. The conditionals find the dictionary needed 
# to process its keys and values. It takes an input that represents the number of the item that is 
# requested to be added to the cart, the name of the item and the department.
def add_items_to_cart(add_input, item, department):
    if department == "groceries":
        def get_dict(groceries):
            return groceries
        department = get_dict(groceries)
    elif department == "appliances":
        def get_dict(appliances):
            return appliances
        department = get_dict(appliances)
    elif department == "furniture":
        def get_dict(furniture):
            return furniture
        department = get_dict(furniture)

    key_list = list(department)
    if item in key_list:
        add_input = item
        cart.append(add_input)
        key_price = department[add_input]
        cart_prices.append(key_price)
    else:
        print("That item is not in the list. Try again.")

    print (f"{add_input} has been added to the cart.")

#Function created to view the items that have been added to the cart and its prices
def view_cart():
    print (f"The items on your cart are:")
    print()
    for number, (cart_items, price) in enumerate(zip(cart, cart_prices), start=1):
        print(f"{number}. {cart_items.capitalize()} - ${price:.2f}")

#Function created to remove items from the cart with its respective prices
def remove_cart_items(remove_input):
    remove_input -= 1
    del cart[remove_input]
    del cart_prices[remove_input]

#Function created to compute the total amount of money of the shopping cart
def compute_total_cart():
    total = sum(cart_prices)
    return total

if __name__ == "__main__":
    main()
        
