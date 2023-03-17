#Import csv for use in program to read/work with csv files
import csv

# Import the datetime class from the datetime
# module so that it can be used in this program.
from datetime import datetime

import random

# Indexes of quantity column in the request.csv file.
PRODUCT_NUMBER = 0
QUANTITY_INDEX = 1

def main():
    
    try:
        with open("request.csv", "rt") as products_file:
            for row in products_file:
                print(row)
    
                """
                *** INSTRUCTIONS FOR MAIN ***
                
                1) Calls the read_dictionary function and stores the compound dictionary in a variable named products_dict.
                2) Prints the products_dict.
                3) Opens the request.csv file for reading.
                4) Skips the first line of the request.csv file because the first line contains column headings.
                5) Uses a loop that reads and processes each row from the request.csv file. Within the body of the loop, does the following for each row:
                    a) Use the requested product number to find the corresponding item in the products_dict.
                    b) Print the product name, requested quantity, and product price.
                    
                Because product number D083 appears twice in the request.csv file, program does not read the request.csv file into a dictionary. Recall that each key in a dictionary is unique. If program reads the request.csv file into a dictionary, when program reads line 3 of the request.csv file, program will put a request for four yogurts into the dictionary. Then when program reads line 6 of the request.csv file, program will replace the request for four yogurts with a request for three yogurts. In other words, if program reads the request.csv file into a dictionary, program will think that the customer ordered only three yogurts instead of the seven (4 + 3) that he ordered. Therefore, program does not read the request.csv file into a dictionary but instead reads and processes each row similar to example 3 in the preparation content for this lesson.
                """
                
                products_dict = read_dictionary('products.csv',PRODUCT_NUMBER) #1 from above
                
                #This is for the store's internal use:
                
                print(f'\n\n')
                print('All Products:')
                
                print(f'\n')
                print(products_dict) #2 from above
                
                #This is the customer's receipt (and for the store's internal use)
                print(f'\n')
                print("Your Receipt from Andrew's Emporium:")
                
                print(f'\n')
                
                # Open a file named request.csv and store a reference to the opened file in a variable named request_file.
                with open("request.csv", "rt") as request_file: #3 from above
                    
                    total_number_items = int(0)
                    subtotal_price = float(0)
                    quantity = int(0)
                    
                    # Use the csv module to create a reader object that will read from the opened file.
                    reader = csv.reader(request_file)

                    # The first row of the CSV file contains column headings and not data about requests, so this statement skips the first row of the CSV file.
                    next(reader)  #4 from above
                
                    # Read each row in the CSV file one at a time.
                    # The reader object returns each row as a list.
                    for row_list in reader: #5 from above
                        
                        prod_number = row_list[PRODUCT_NUMBER]
                        prod_name = products_dict[prod_number][1]
                        prod_price = float(products_dict[prod_number][2])
                        
                        # For the current row, retrieve the requested quantity.
                        quantity = int(row_list[QUANTITY_INDEX]) #5A from above
                        
                        print(f'{prod_name}: {quantity} @ ${prod_price}') #5B from above
                        
                        total_number_items = quantity + total_number_items
                        subtotal_price += (prod_price * quantity)
                        sales_tax = subtotal_price*.06
                        total_price = subtotal_price + sales_tax
                        

                
                print(f'\n')
                print(f'Number of Items: {total_number_items}')
                print(f'Subtotal: {subtotal_price:.2f}')
                print(f'Sales Tax: {sales_tax:.2f}')
                print(f'Total: {total_price:.2f}')
                
                print(f'\n')
                print("Thank you for shopping with us today")

                # Call the now() method to get the current
                # date and time as a datetime object from
                # the computer's operating system.
                current_date_and_time = datetime.now()

                # Use an f-string to print the current
                # day of the week and the current time.
                # Prints in this format: Wed Nov  4 05:10:30 2020   
                print(f'{current_date_and_time:%a %b %d %H:%M:%S %Y}')
        
                
                print(f'\n\n')


    except FileNotFoundError as not_found_err:
        print(not_found_err)
        
    except PermissionError as perm_err:
        print(f"Error: cannot read file because you don't have permission.")
        
    except KeyError as key_err:
        print(type(key_err).__name__, key_err)      

def read_dictionary(filename, key_column_index):
    """
    *** INSTRUCTIONS FOR READ_DICTIONARY ***
    
    write a function named read_dictionary that will open a CSV file for reading and use a csv.reader to read each row and populate a compound dictionary with the contents of the products.csv file.
    
    Example of the returned format from products dictionary will be:
        Key	= "D150"
        Value = ["D150", "1 gallon milk", 2.85]    

    *** DOCUMENTATION STRING ***
    
    Read the contents of a CSV file into a compound dictionary and return the dictionary.

    Parameters
        filename: the name of the CSV file to read.
        key_column_index: the index of the column to use as the keys in the dictionary.
    Return: a compound dictionary that contains the contents of the CSV file.
    """
    
    product_dictionary = {}
    
    # Open a file named products.csv and store a reference to the opened file in a variable named products_file.
    with open(filename, "rt") as products_file:
    
        # Use the csv module to create a reader object that will read from the opened file.
        reader = csv.reader(products_file)

        # The first row of the CSV file contains column headings and not data about requests, so this statement skips the first row of the CSV file.
        next(reader)  #4 from above
    
        # Read the rows in the CSV file one row at a time.
        # The reader object returns each row as a list.
        for row_list in reader:

            # If the current row is not blank, add the data from the current to the dictionary.
            if len(row_list) != 0:

                # From the current row, retrieve the data from the column that contains the key.
                key = row_list[key_column_index]

                # Store the data from the current row into the dictionary.
                product_dictionary[key] = row_list
        
        return product_dictionary
    
    
# If this file was executed like this: > python teach_solution.py then call the main function. 
# However, if this file was simply imported, then skip the call to main.
if __name__ == "__main__":
    main()
    
    
# NOTE - for both the receipt.py file and the test_products.py file to work, these and the request.csv and products.csv files all need to be housed in the main folder, not week 9.
    