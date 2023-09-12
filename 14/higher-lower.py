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
  desc = data_point["description"]
  country = data_point["country"]
  return f"{name}, a {desc}, from {country}."

def prompt_user_input():
  return input("Who has more followers? Type 'A' or 'B': ")

def who_has_more_followers(A, B):
  if A["follower_count"] > B["follower_count"]:
    return 'A'
  return 'B'

def round(A,B, current_score):
  print(logo)
  if current_score != 0 :
    print(f"You're right! Current score is: {current_score}")
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

# Draw inital data points:
A = get_data_point()
B = get_data_point()

# Gameplay part:
while keep_playing:
  round_result = round(A,B, score)
  score += round_result
  if round_result == 0:
    keep_playing = False
  else:
    A = B
    B = get_data_point()
    
print(logo)
print(f"Your score is: {score}")
