rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random

# Match results
match_results = ["draw", "win" , "lose"]

# Drawing mapping
drawings = [rock, paper, scissors]

# Prompt player
msg = "What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."
print(msg)

# Take player choice
player_input = input()

# Convert to int
player_choice = int(player_input)
if(player_choice >=3 or player_choice <=0):
  print("You entered an invalid number, you lose.")
  exit()

print(drawings[player_choice])

# Generate computer choice
computer_choice = random.randint(0,2)
print("Computer chose:")
print(drawings[computer_choice])

# Calculate match outcome:
match_outcome = (player_choice - computer_choice) % 3

# Print reuls
print(f"You {match_results[match_outcome]}")