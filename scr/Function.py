from tabulate import tabulate
import csv
import os
import sys

# Specify the path to the CSV file
csv_file_path = 'Data/Database_Filtered.csv'

# Open the CSV file in read mode
def initialize_db():
    with open(csv_file_path, 'r') as file:
        # Create a CSV reader object with dictionary format
        reader = csv.reader(file, delimiter=",")
        database = {}
        # Mengisi data ke dalam database
        for row in reader:
            name,crystal_stucture ,diaphaneity,specific_gravity,optical,refractive_index,\
                molar_mass, molar_volume, calculated_density = row
            database.update({name:{
                                   'Crystal Structure': crystal_stucture,
                                   'Diaphaneity': diaphaneity,
                                   'Specific Gravity': specific_gravity,
                                   'Optical':optical,
                                   'Refractive Index':refractive_index,
                                   'Molar Mass':molar_mass,
                                   'Molar Volume': molar_volume,
                                   'Calculated Density': calculated_density}})
    return (database)

# Formatting Tabel
def convert_to_table(data, columns, title):
    """
    Function to change database to table format
    """
    # Table title
    print(title)

    # Changes to table format
    print(tabulate(data, headers=columns, tablefmt="grid"))

# Show database as table
def show (table):
    """
    Function to show the database to table format
    """

    # Showing database minerals as table
    convert_to_table(
        data= [[outer, *inner.values()] for outer, inner in table.items()],
        columns=['Name', 'Crystal Structure','Diaphaneity','Specific Gravity','Optical',\
                 'Refractive Index','Molar Mass','Molar Volume','Calculated Density'],
        title='\nMinerals Database\n'
    )


# Alphabert validation
def valid_alpha (task):
    """
    Function to make sure that the input is alphabert

    """
    while True:
        #Input word
        word = input(task).title()
        #If input is alphabert
        if word.isalpha():
            break
        #If input not alphabert
        else:
            print ('Just input letters!')
            continue

    return word

# Integer validation
def valid_int (task):
    """
        Function to make sure that the input is integers
    """
    while True:
        try:
            #Input number
            nums = int (input (task))
            #If number negative
            if nums >= 0:
                break
            else:
                print ('Input must be positive!')
                continue
        except:
            #If input not numbers
            print ('Just input numbers')
        continue
    return nums

# Show database base on mineral name
def show_filtered(table):
    """
        Function to show database mineral base on name
    """
    while True:
        # Input mineral name
        input_min = input('Input mineral name: ').capitalize()
        #If mineral in database
        if input_min in table.keys():
            filtered_table = table.copy()
            filtered_table = dict(filter(lambda item: item[0] == input_min, filtered_table.items()))
            crystal_structure(filtered_table,input_min)
            diaphaneity(filtered_table,input_min)
            optical(table,input_min)
            break
        #If mineral not in database
        else:
            print ("I'm sorry, mineral you looking for is not in database!, want to back to main menu?")
            

            main()
    show (filtered_table)

# Change crystal stucture information
def crystal_structure(table,input_min):
    """
        Function to change the information of crystal structure
    """
    if table[input_min]['Crystal Structure'] == '1.0':
        table[input_min]['Crystal Structure']='Triclinic'
    elif table[input_min]['Crystal Structure'] == '2.0':
        table[input_min]['Crystal Structure']= 'Monoclinic'
    elif table[input_min]['Crystal Structure'] == '3.0':
        table[input_min]['Crystal Structure']= 'Orthorhombic'
    elif table[input_min]['Crystal Structure'] == '4.0':
        table[input_min]['Crystal Structure']= 'Tetragonal'
    elif table[input_min]['Crystal Structure'] == '5.0':
        table[input_min]['Crystal Structure']= 'Hexagonal'
    elif table[input_min]['Crystal Structure'] == '6.0':
        table[input_min]['Crystal Structure']= 'Trigonal'
    elif table[input_min]['Crystal Structure'] == '7.0':
        table[input_min]['Crystal Structure']= 'Cubic'
    elif table[input_min]['Crystal Structure'] == '8.0':
        table[input_min]['Crystal Structure']= 'Amorphous'
    else:
        table[input_min]['Crystal Structure']= "-"

# Change diaphaneity information
    """
        Function to change the information of diaphaneity
    """  
def diaphaneity(table,input_min):
    if table[input_min]['Diaphaneity'] == '1.0':
        table[input_min]['Diaphaneity']='Opaque'
    elif table[input_min]['Diaphaneity'] == '2.0':
        table[input_min]['Diaphaneity']= 'Translucent'
    elif table[input_min]['Diaphaneity'] == '3.0':
        table[input_min]['Diaphaneity']= 'Transparent'
    else:
        table[input_min]['Diaphaneity']= "-"


# Change optical information
    """
        Function to change the information of optical
    """  
def optical(table,input_min):
    if table[input_min]['Optical'] == '1.0':
        table[input_min]['Optical']='Anisotropic'
    elif table[input_min]['Optical'] == '2.0':
        table[input_min]['Optical']= 'Isotropic'
    elif table[input_min]['Optical'] == '3.0':
        table[input_min]['Optical']= 'Uniaxial'
    elif table[input_min]['Optical'] == '3.0':
        table[input_min]['Optical']= 'Biaxial'
    else:
        table[input_min]['Optical']= "-"

# Clear user screen
def clear_screen():
    """
    A function to clean the user interface
    """
    # For Windows
    if os.name == 'nt':
        _ = os.system('cls')
    # For macOS and Linux
    else:
        _ = os.system('clear')

# Main program
def main():
    """
    A function to run the main program
    """
    global database
    clear_screen()
    while True:
        print (
'''
-------------------
Minerals Database:
Input your choice :
1. Find Minerals
2. Exit
-------------------
         ''')
        choice =valid_int('Input your choice: ')
        if choice == 1:
            show_filtered(database)
        elif choice == 2:
            sys.exit()
        else:
            print ('Your input not available, choose (1/2): ')
            continue


# Initializing database
database = initialize_db()
