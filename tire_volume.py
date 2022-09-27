import math
from datetime import datetime

current_date_and_time = datetime.now()
print(f"{current_date_and_time:%Y-%m-%d}")


width = int(input("Enter the width of the tire in mm (ex 205): "))
ratio = int(input("Enter the aspect ratio of the tire (ex 60): "))
diameter = int(input("Enter the diameter of the wheel in inches (ex 15): "))

volume = (math.pi * (width**2) * ratio * (width * ratio + (2540 * diameter))) / 10000000000

print (f"The approximate volume is {volume:.2f} liters")


buy_tires = input("Do you want to buy tires with the dimention entered? ").lower()
if buy_tires == "yes":
    phone_number = input("Please enter your phone number: ")
    with open("volumes.txt", "at") as volumes_file:
        print(f"{current_date_and_time:%Y-%m-%d}, {width}, {ratio}, {diameter}, {volume:.2f} Customer interested: {phone_number}", file=volumes_file)
else:
    with open("volumes.txt", "at") as volumes_file:
        print(f"{current_date_and_time:%Y-%m-%d}, {width}, {ratio}, {diameter}, {volume:.2f}", file=volumes_file)




