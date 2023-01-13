#==============Library import================
import pandas as pd
#========The beginning of the class==========
class Shoe():
    '''
    In this function, you must initialise the following attributes:
        ● country,
        ● code,
        ● product,
        ● cost, and
        ● quantity.
    '''
    def __init__(self, country, code, product, cost, quantity):
        pass
        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity

    def get_cost(self):
        pass
        '''
        Add the code to return the cost of the shoe in this method.
        '''
        return self.cost

    def get_quantity(self):
        pass
        '''
        Add the code to return the quantity of the shoes.
        '''
        return self.quantity

    def __str__(self):
        pass
        '''
        Add a code to returns a string representation of a class.
        '''
        return f"{self.product} from {self.country} with code {self.code} costs {self.cost} and there are {self.quantity} in stock"


#=============Global variables===========

#The list will be used to store a list of objects of shoes.
shoe_list = []

#==========Functions outside the class==============
def read_shoes_data():
    pass
    '''
    This function will open the file inventory.txt
    and read the data from this file, then create a shoes object with this data
    and append this object into the shoes list. One line in this file represents
    data to create one object of shoes. You must use the try-except in this function
    for error handling. Remember to skip the first line using your code.
    '''
    # start with an empty list
    global shoe_list
    shoe_list = []
    try:
        with open("inventory.txt", "r") as f:
            # skip the first line
            f.readline()
            # read the remaining lines
            for line in f:
                country, code, product, cost, quantity = line.strip().split(",")
                shoe = Shoe(country, code, product, float(cost), int(quantity))
                shoe_list.append(shoe)
    except Exception as e:
        print(f"Error reading data from file: {e}")
    return shoe_list

def capture_shoes():
    pass
    '''
    This function will allow a user to capture data
    about a shoe and use this data to create a shoe object
    and append this object inside the shoe list.
    '''
    # Defensive programming elements prevent wrong inputs by the user. 
    # Capture country input
    while True:
        try:
            country = str(input("Enter the country of manufacture: "))
            break
        except ValueError:
            print("Invalid input. Please try again.")
    # Capture code input
    while True:
        try:
            code = str(input("Enter the code of the shoe: "))
            break
        except ValueError:
            print("Invalid input. Please try again.")
            
    while True:
        try:
            product = str(input("Enter the product name: "))
            break
        except ValueError:
            print("Invalid input. Please try again.")

    while True:
        try:
            cost = float(input("Enter the cost of the shoe: "))
            break
        except ValueError:
            print("Invalid input. Please try again.")

    while True:
        try:
            quantity = int(input("Enter the quantity: "))
            break
        except ValueError:
            print("Invalid input. Please try again.")

    # Create Shoe object
    shoe = Shoe(country, code, product, cost, quantity)

    # Append Shoe object to list
    shoe_list.append(shoe)
    return

    

def view_all():
    pass
    '''
    This function will iterate over the shoes list and
    print the details of the shoes returned from the __str__
    function. Optional: you can organise your data in a table format
    by using Python’s tabulate module.
    '''
    # Initialise a list that will store objects' attributes
    data = []
    # Iterate through shoe_list and add each object attributes to the data list
    for shoe in shoe_list:
        data.append([shoe.country, shoe.code, shoe.product, shoe.cost, shoe.quantity])
    # Build the dataframe from the data store in the list
    df = pd.DataFrame(data, columns=['Country', 'Code', 'Product', 'Cost', 'Quantity'])
    # Add a column that calculates the total value of the inventory (Cost * Quantity)
    value_per_item(df)
    # Print the output dataframe
    print(df)
    return

def re_stock():
    pass
    '''
    This function will find the shoe object with the lowest quantity,
    which is the shoes that need to be re-stocked. Ask the user if they
    want to add this quantity of shoes and then update it.
    This quantity should be updated on the file for this shoe.
    '''
    # Initiate an unbound variable to use as starting point to find the min quantity value
    min_quantity = float('inf')
    # Initiate variable that will store the object with the lowest stock quantity
    min_shoe = None
    # Iterate through the shoe list to find the shoe object with the lowest stock quantity
    for shoe in shoe_list:
        if shoe.quantity < min_quantity:
            min_quantity = shoe.quantity
            min_shoe = shoe
    # Display min_shoe to the user
    print("Please review the item with lowest stock levels:\n", end = '')
    print(min_shoe) 
    # Ask the user if they want to add shoes to the stock
    while True:
        su_answer = str(input('Do you want to add shoes to the stock? (Y/N)'))
        # If the user answer y, then ask how many would like to add and update the object
        if su_answer.lower() == 'y':
            while True:
                try:
                    num_to_add = int(input('How many shoes do you want to add? '))
                    break
                except ValueError:
                    print("Invalid input. Please enter a valid number.")
            min_shoe.quantity += num_to_add
            break
        # Exit the while loop if the users answers n
        elif su_answer.lower() == 'n':
            break
        # If the answer is not value display an error message and ask the user to try again
        else:
            print('Please enter a valid option (Y/N)')
    return

def seach_shoe():
    pass
    '''
     This function will search for a shoe from the list
     using the shoe code and return this object so that it will be printed.
    '''
    # Initiate variable that will store the shoe found by the search
    seach_shoe = None
    # Iterate until the user input a valid code or enter -1 to return to the main menu
    while True:
        # Request product code or exit command from the user
        product_code = str(input("Please enter the code of the product you want to search (Enter -1 to return to the main menu): "))
        
        # Iterate through the shoe_list and check if a shoe code matches the code entered by the user
        for shoe in shoe_list:
            if shoe.code == product_code:
                seach_shoe = shoe
        
        # Exit the loop if the user enter -1
        if product_code == "-1":
            break
        # Check if the seach_shoe is not none. Thus, exit the loop since the shoe was found
        elif seach_shoe != None:
            break
        # Otherwise the code was not found, ask the user to try again
        else:
            print("Product not found. Please try again.")
    return seach_shoe

# This function was added to the view_all() function since I believe the totals could be shown at all tables in the table view
# The task says get creative!
def value_per_item(df):
    pass
    '''
    This function will calculate the total value for each item.
    Please keep the formula for value in mind: value = cost * quantity.
    Print this information on the console for all the shoes.
    '''
    df['Total value'] = df['Cost'] * df['Quantity']
    return df

def highest_qty():
    pass
    '''
    Write code to determine the product with the highest quantity and
    print this shoe as being for sale.
    '''
    #Initiate an unbound variable to use as starting point to find the max quantity value
    max_quantity = float('-inf')
    # Initiate variable that will store the object with the lowest stock quantity
    max_shoe = None
    # Iterate through the shoe list to find the shoe object with the lowest stock quantity
    for shoe in shoe_list:
        if shoe.quantity > max_quantity:
            max_quantity = shoe.quantity
            max_shoe = shoe
    # Return the sales launch message
    return f"The {max_shoe.product} shoe from {max_shoe.country} is going of sale at a 20% discount."

def update_inventory(shoe_list):
    """
    Every change in the class objects and their attributes are reflected in the shoe_list. Therefore, it holds 
    the latest version of the data. The function takes the list ob objects shoe_list as an argument and rewrites 
    the file using the attributes of the list object. The function will be used on instances where an object from 
    the list is modified, so the change is reflected on the database.
    """
    with open("inventory.txt", "w") as f:
        # write the header line
        f.write("Country,Code,Product,Cost,Quantity\n")
        # write a line for each shoe object
        for shoe in shoe_list:
            f.write(f"{shoe.country},{shoe.code},{shoe.product},{shoe.cost},{shoe.quantity}\n")

#==========Main Menu=============
'''
Create a menu that executes each function above.
This menu should be inside the while loop. Be creative!
'''
# Run the read_shoe_data function to load available stock data on startup
read_shoes_data()
print(shoe_list[18].quantity)
# Initiate the variable that will store user menu choice
menu_choice = ""
# The while loop will display the menu until the user chooses to exit the program
# The program will return to menu after completing each task. 
while menu_choice != "7":
    
    menu_choice = str(input("""
====================================
Select one of the following options 
below by choosing its number:
1. Update shoe list from database
2. Add stock entry
3. Code search SKU
4. Display stock data
5. Re-stock tool
6. Run atumated sale
7. Exit
====================================
"""))
    
    if menu_choice == '1':
        """read the inventory file again in case new items have been added 
        directly to the database while the program was running."""
        # Run read_shoes_data to update shoe_list from database
        read_shoes_data()

    elif menu_choice == '2':
        # Run function that allos user to input a new item and add it to shoe_list
        capture_shoes()
        # update the inventory.txt file
        update_inventory(shoe_list)

    elif menu_choice == '3':
        # Print search output for the user
        print(seach_shoe())

    elif menu_choice == '4':
        # Run the function to display stock data
        view_all()

    elif menu_choice == '5':
        # Run function to allow the user to determine if a product needs a re-stock
        re_stock()
        # update the inventory.txt file
        update_inventory(shoe_list)

    elif menu_choice == '6':
        # Print the return message of the highest_qty function, once the function have identified the shoe with highest stock level.
        print(highest_qty())

    elif menu_choice == '7':
        print("Goodbye!!")
    else:
        print("Invalid choice. Try again.")
