from art import logo
import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
player_cards = []
computer_cards = []


def draw_card():
  return [random.choice(cards)]

# prompts player for a game
def play_another_game():
  play_game_input = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
  if play_game_input == 'y':
    return True
  return False

# deal cards. 
def deal_inital_hand():
  player1 = [random.choice(cards), random.choice(cards)]
  player2 = [random.choice(cards), random.choice(cards)]
  return (player1, player2)

def deal():  
  (p1,p2) = deal_inital_hand()
  if sum(p1) < 17:
    p1 += draw_card()
  # print(p1)
  return (p1,p2)
  
deal()

# prompt hit
def to_hit():
  hit_input = input("Type 'y' to get another card, type 'n' to pass: ")
  if hit_input == 'y':
    return True
  return False



# Evaluate score.
def calc_score(player_hand):
  return sum(player_hand)

# TODO: Implement logic accoring to chart


# Prompt for game:
play_game = play_another_game()

while play_game:
  
  print(logo)
  
  (computer_cards, player_cards) = deal()

  # print hands
  print(f"    Your cards: {player_cards}, current score: {calc_score(player_cards)}")
  print(f"    Computer's first card: {computer_cards[0]}")
  
  # prompt hit
  did_hit = to_hit()
  while to_hit():
    
    #draw
    draw_card()
    
    # check score
    
    # prompt additional hit
    
  # Evaluate score
  
  # print win or lose.
  
  # prompt additional game.