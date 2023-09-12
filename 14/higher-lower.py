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


from art import logo, vs
from game_data import data
from random import randint
from os import system

data_index_size = len(data) - 1
score = 0
keep_playing = True


def get_data_point():
  return data[randint(0, data_index_size)] 

def stringify_data(data_point):
  name = data_point["name"]
  # followers = data_point["follower_count"]
  desc = data_point["description"]
  country = data_point["country"]
  return f"{name}, a {desc}, from {country}."

def prompt_user_input():
  return input("Who has more followers? Type 'A' or 'B': ")

def who_has_more_followers(A, B):
  if A["follower_count"] > B["follower_count"]:
    return 'A'
  return 'B'

def round(A,B):
  print(f"Compare A: {stringify_data(A)}")
  print(vs)
  print(f"Against B: {stringify_data(B)}")
  user_guess = prompt_user_input()
  correct_answer = who_has_more_followers(A, B)
  system('cls')
  if user_guess == correct_answer:
    return 1
  else:
    return 0

# Program start
print(logo)

# Draw inital data points:
A = get_data_point()
B = get_data_point()

# print(A)
# print(B)

# Gameplay part:
while keep_playing:
  round_result = round(A,B)
  score += round_result
  if round_result == 0:
    keep_playing = False
  else:
    A = B
    B = get_data_point()
    
print(logo)
print(f"Your score is: {score}")
# reapting section
# 1. create a function to print data points. 
# 2. create a function to prompt user for input
# 3. create a function for the evaluating user guess
# 4. add score tracking. 
# 5. wrap it up in a while loop. 