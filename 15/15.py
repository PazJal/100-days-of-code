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
    


print("Hello, Please order your coffee.")
print_report()

print(input_money())

# TODO: Create general order prompt


# TODO: Create a function to test the resources



