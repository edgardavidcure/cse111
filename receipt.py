import csv
from datetime import datetime

requested_product_number_index = 0
requested_product_quantity_index = 1
store_name = "Inkom Emporium"


def main():
    try:
        product_number_index = 0
        products_dict = read_dict("products.csv", product_number_index )
        print()
        print(store_name)
        print()
        print("Items")
        total_quantity_requested = 0
        
        with open("request.csv", "rt") as request_file:
            reader = csv.reader(request_file)
            next(reader)
            subtotal = 0
           

            for row in reader:
                
                product_requested = row[requested_product_number_index]
                quantity_requested = int(row[requested_product_quantity_index])
                
                
                
                
                value = products_dict[product_requested]
                product_name = value[1]
                product_price = float(value[2])
                print(f"{product_name}: {quantity_requested} @ {product_price}")
                total_quantity_requested += quantity_requested
                
                subtotal_per_item = quantity_requested * product_price
                subtotal +=subtotal_per_item
                
                

            

            

            date = datetime.now()
            weekday = date.weekday()
            if weekday == 1 or weekday == 2:
                print()
                print(f"Number of items:", total_quantity_requested)
                discount = subtotal * 0.1
                subtotal = subtotal - discount
                sales_tax = subtotal * 0.06
                total = subtotal + sales_tax
                print("Congratulations! It is Thursday and you get a 10% discount")
                print(f"Your subtotal with discount is:  {subtotal:.2f}")
                print(f"Sales tax: {sales_tax:.2f}")
                print(f"Total: {total:.2f}")
                
            else:
                print()
                print(f"Number of items:", total_quantity_requested)
                sales_tax = subtotal * 0.06
                total = subtotal + sales_tax
                print(f"Sales tax: {sales_tax:.2f}")
                print(f"Total: {total:.2f}")
                
             
            print()
            
        
            print()
            print("Thanks for shopping at the Inkom Emporium.")
            
            print(f"{date:%a %b %d %I:%M %p %Y }")
            print()
            
            
    

                
    except FileNotFoundError as fil_err:
        print(fil_err)
        print("Choose a different file")
        
    except PermissionError as permission_err:
        print(permission_err)
        print("Choose a different file")

    except KeyError as key_err:
        print(f"Error: unknown product ID in the request.csv file")
        print(key_err)
    

  


def read_dict(filename, key_column_index):
    """Read the contents of a CSV file into a compound
    dictionary and return the dictionary.

    Parameters
        filename: the name of the CSV file to read.
        key_column_index: the index of the column
            to use as the keys in the dictionary.
    Return: a compound dictionary that contains
        the contents of the CSV file.
    """
    products = {}

    with open(filename, "rt") as products_file:
        
        reader = csv.reader(products_file)

        next(reader)

        for row in reader:

            key = row[key_column_index]
            products[key] = row

    return products


if __name__ == "__main__":
    main()

