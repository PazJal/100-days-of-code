import random

# Choose Difficulty
def choose_difficulty():
  """Returns number of lives according to difficulty chosen.

  Returns:
      _int_: Numbers of lives according to difficulty chosen
  """  
  user_input = input("Select a difficulty. Type 'easy' or 'hard': ")
  if user_input == 'easy':
    return 10
  if user_input == 'hard':
    return 5
  return 5


# Prompt attmpets remaining
def print_attempts_remaining(attempts):
  print(f"You have {attempts} attempts remaining.")


# Guess
def guess():
  """Receives user guess

  Returns:
      _int_: users input converted to an integer
  """  
  user_input = int(input("Make a guess: "))
  return user_input


# Guess Feedback & update attempts
def compare_guess(guess):
  """_summary_

  Args:
      guess (_int_): user guess

  Returns:
      _int_: Amount of attempts left or -1 if user has guessed the number. 
  """  
  if guess == number:
    # Handle win condition
    return -1
  elif guess > number:
    # Handle over guess. 
    print("Too high.")
  else:
    # handle uner guess.
    print("Too low.")
  return lives - 1


# Choose a random number. 
number = random.randint(1,100)

#  Welcome prompt
print("Welcome to the guessing game!")

lives = choose_difficulty()

continue_playing = True

while continue_playing:
  
  print_attempts_remaining(lives)
  current_guess = guess()
  lives = compare_guess(current_guess)  
  # Win lose conditions.
  if lives == -1:
    print(f"You guessed it the number was: {number}")
    continue_playing = False
  if lives == 0:
    print(f"You lost! The number was {number}")
    continue_playing = False