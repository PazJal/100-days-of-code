from art import logo
import math

def add(n1, n2):
  return n1 + n2
def subtract(n1, n2):
  return n1 - n2
def multiply(n1, n2):
  return n1 * n2
def divide(n1, n2):
  if n2 != 0:
    return n1 * n2
  return math.nan

operations = {
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide,
}


def calculator():
  print(logo)
  num1 = float(input("What's the first number?: "))

  for key in operations:
    print(key)

  operation_symbol = input("Pick an operation from the line above: ")

  num2 = float(input("What's the second number?: "))

  first_answer = operations[operation_symbol](num1, num2)

  print(f"{num1} {operation_symbol} {num2} = {first_answer}")
  
  should_contine = True

  # continue_calculation = input(f"Type 'y' to continue calculating with {first_answer} or type 'n' to exit.: ")

  while should_contine:
    
    operation_symbol = input("Pick an operation: ")

    num3 = float(input("What's the next number?: "))

    second_answer = operations[operation_symbol](first_answer, num3)

    print(f"{first_answer} {operation_symbol} {num3} = {second_answer}")
    
    first_answer = second_answer
    
    continue_calculation = input(f"Type 'y' to continue calculating with {first_answer} or type 'n' to start a new calculation: ")
    if continue_calculation == 'n':
      should_contine = False
      calculator() # This is a very bad way to restart the calculator>?
calculator()