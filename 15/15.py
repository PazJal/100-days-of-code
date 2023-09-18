MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

ESPRESSO = "espresso"
LATTE = "latte"
CAPPUCCINO = "cappuccino"

money = 0

# a function to print report
def print_report():
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${money}")

# Get the conins input and return the money amount. 
def input_money():
    quarters = int(input("how many quarters?: "))
    dimes = int(input("how many quarters?: "))
    nickles = int(input("how many quarters?: "))
    pennies = int(input("how many quarters?: "))
    
    return (quarters * 0.25 + dimes * 0.1 + nickles * 0.05 + pennies * 0.01)
    
# general order prompt
def select_operation():
    """Returns user selection from the menu. 

    Returns:
        string: the users choice. 
    """    
    
    operation = input("What would you like? ('e' for espresso, 'l' for latter, 'c' for cappuccino): ")
    return operation

def has_resources(drink_selected):
    """Checks if the machine has enough resources to make the drink

    Args:
        drink_selected (string): the selected drink

    Returns:
        boolean: True if there are the resources needed to make the drink
    """    
    
    drink = MENU[drink_selected]["ingredients"]
    if drink["water"] > resources["water"]:
        return False
    elif drink["milk"] > resources["milk"]:
        return False
    elif drink["coffee"] > resources["coffee"]:
        return False
    return True

def has_money(money, drink_selected):
    drink = MENU[drink_selected]
    if drink["cost"] > money:
        return False
    return True

def get_drink_cost(drink):
    return MENU[drink]["cost"]


def can_make_drink(money, drink):
    """Tests if we can make the drink. 

    Args:
        money (float): _description_
        drink (enum): _description_

    Returns:
        boolean: returns true if it is possible to make the drink
    """
    
    # TODO: Check on the correct order to implement this
    
    # Test moeny
    if not has_money(money, drink):
        print("Not enough money.")
        return False
    # Test resources
    if not has_resources(drink):
        # TODO:: Test if we need the specific resource missing. 
        print("Does not have enough resources.")
        return False
    # Making the drink
    print("Making the drink. ")
    return True
    
    

# TODO: Implement general flow. 

dont_quit = True
print("Hello, Please order your coffee.")

while dont_quit:
    #Prompt for user choice
    drink = ""
    current_amount = 0
    user_selection = select_operation()
    if user_selection == 'q':
        dont_quit = False
        continue
    elif user_selection == 'r':
        print_report()
        continue
    elif user_selection == 'l':
        drink = LATTE
    elif user_selection == 'c':
        drink = CAPPUCCINO
    elif user_selection == 'e':
        drink = ESPRESSO
    
    #prompt for money
    current_amount = input_money()
    
    # make drink
    if can_make_drink(current_amount, drink):
        
        # TODO: Remove the correct amounts from the resouces
        print(f"Making {drink}")
        # TODO: Return the correct amount to the client and update the money. 
        

        # if(has_resources("latte") and has_money(money, "latte")):
            # print("Making latte")
        
        

# print_report()

# print(input_money())



# TODO: Create a function to test the resources



