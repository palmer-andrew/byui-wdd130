import csv


# Each row in the pupils.csv file contains three elements.
# These are the indexes of the elements in each row.
GIVEN_NAME_INDEX = 0
SURNAME_INDEX = 1
BIRTHDATE_INDEX = 2

def main():
    try:
        #4A Call the read_compound_list function to read the pupils.csv file into a list named students_list.
        
        students_list = read_compound_list('pupils.csv')
        
        #4B Write a lambda function that will extract the birthdate from a student.
        
        extract_birthdate = lambda student: student[GIVEN_NAME_INDEX]
        
        #4C Write a call to the Python built-in sorted function that will sort the students_list by birthdate from oldest to youngest.
        
        sorted_list = sorted(students_list, key=extract_birthdate)
        
        #4D Print the students_list by calling the print_list function.
        
        print_list(sorted_list)
    
    except (FileNotFoundError, PermissionError) as error:
        print(type(error).__name__, error, sep=": ")

def read_compound_list(filename):
    """Read the text from a CSV file into a compound list.
    The compound list will contain small lists. Each small
    list will contain the data from one row of the CSV file.

    Parameter
        filename: the name of the CSV file to read.
    Return: the compound list
    """
    # Create an empty list.
    compound_list = []

    # Open the CSV file for reading.
    with open(filename, "rt") as csv_file:

        # Use the csv module to create a reader
        # object that will read from the opened file.
        reader = csv.reader(csv_file)

        # The first line of the CSV file contains column headings
        # and not a student's I-Number and name, so this statement
        # skips the first line of the CSV file.
        next(reader)

        # Process each row in the CSV file.
        for row in reader:

            # Append the current row at the end of the compound list.
            compound_list.append(row)

    return compound_list

#3 Write a function named print_list that takes a list as a parameter and prints each element of the list on a separate line. In other words, this print_list function should include a for loop that prints each element on a separate line.

def print_list(compound_list):
    for element in compound_list:
        print(element)
    print()

#5 At the bottom of the pupils.py file write a call to the main function.
if __name__ == "__main__":
    main()