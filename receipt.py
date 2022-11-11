import csv

requested_product_number_index = 0
requested_product_quantity_index = 1


def main():
    product_number_index = 0
    products_dict = read_dict("products.csv", product_number_index )
    print(products_dict)
    print()
    print("Requested Items")
    
    with open("request.csv", "rt") as request_file:
        reader = csv.reader(request_file)
        next(reader)

        for row in reader:
            product_requested = row[requested_product_number_index]
            quantity_requested = int(row[requested_product_quantity_index])
            
            if product_requested in products_dict:
                value = products_dict[product_requested]
                product_name = value[1]
                product_price = float(value[2])
                print(f"{product_name}: {quantity_requested} @ {product_price}")

                


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

