#For more info about try: and except: go to: https://www.w3schools.com/python/python_try_except.asp
#Or, just wait for the lesson in a few weeks!

from datetime import datetime

current_time = datetime.now()
weekday = current_time.weekday()
#weekday = 0 #Uncomment me for having no discount!
#weekday = 1 #Uncomment me for a discount!

new_cost = ""
sub_total = 0.00
#Main while loop
while(new_cost != 0):
    got_input = False #Got input is the only way to get out of the loop
    #Protected input loop for price
    while(not got_input):
        try: #Try this code, if it throws an error, catch it! (It's structured like an if statement!)
            new_cost = float(input("Please enter the price of the item: $"))#This block will end here if there was a value error, new_cost will not be changed
            #If the user enters something that doesn't convert to a float, it will produce a valueError which will end this code early, and go to the "except ValueError"
            if(new_cost > 0): #We have a positive number
                got_input = True #This loop can end now
            elif(new_cost == 0): #We want the main while loop to end when the user enters $0.00 as the price
                break #Go to the main while loop
            else: #Negative number
                print("Invalid number, please try again!") #You could say, "not a positive number, please try again!"
        #"except NameOfError:"" or you can just do "except:" to catch all errors
        except ValueError: #When we have a ValueError, do this code!
            print("Not a number, please try again!")
    if(new_cost == 0): #New cost == 0? That means we left the last protected input early
        break #Exit the main while loop
    #Protected input loop for item count
    got_input = False #Loop ending condition
    while(not got_input):
        try:#Try to run this code
            num_item = float(input("Please input the quantity of the item: "))#This block will end here if there was a value error, num_item will not be changed
            #There's something we forgot to do here, see if you can figure it out (hint: there's a number that we probably don't want)
            if(num_item >= 0): #We want a positive value
                got_input = True #End the loop, the value is correct
            else:#Negative value
                print("Invalid number, please try again!")
        except ValueError:#Do this when there's a value error
            print("Not a number, please try again!")
    sub_total += (new_cost * num_item)
    #There's a way to clear the console window every time this loop runs using the system's normal console clear command (it's different depending on the Operating System (ex. windows, mac, linux))
    #but it'd require the print("Subtotal: {sub_total:.2f}") at the top of the while loop
    print(f"Current Subtotal: ${sub_total:.2f}") 
discount = 0.0

if((weekday == 1 or weekday == 2) and sub_total >= 50.00):
    discount = sub_total * 0.1
    print(f"Discount amount: ${discount:.2f}")
elif((weekday == 1 or weekday == 2) and sub_total < 50.00):
    print(f"You are ${50.00 - sub_total:.2f} under the discount amount.")
sub_total -= discount
taxes = sub_total * 0.06
total = sub_total + taxes

print(f"Sales tax amount: ${taxes:.2f}")
print(f"Total: ${total:.2f}")