# Game overview:

# Initialize - choose two points to compare. 

# repeating section:
  
#   Player makes a guess. 
#   Player is either eliminated or moves to next stage. 
  
#   make second data point first data point
#   draw a new data point. 

# Initialize game
  # -[x] Print logo
  # -[x] Draw 2 data points. 


from art import logo
from game_data import data
from random import randint

data_index_size = len(data) - 1

def get_data_point():
  return data[randint(0, data_index_size)]


# Program start
print(logo)


# Draw data points:


A = get_data_point()
B = get_data_point()

print(A)
print(B)