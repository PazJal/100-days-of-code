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
  player1 = draw_card()
  player2 = draw_card() + draw_card()
  return (player1, player2)

def resolve_dealer_hand(dealer_hand):  
  while sum(dealer_hand) < 17:
    dealer_hand += draw_card()
  
  return dealer_hand
  
# prompt hit
def to_hit():
  hit_input = input("Type 'y' to get another card, type 'n' to pass: ")
  if hit_input == 'y':
    return True
  return False
# Evaluate score.
def calc_score(player_hand):
  if len(player_hand) == 2 and sum(player_hand) == 21:
    return 0
  number_of_aces = player_hand.count(11)
  current_score = sum(player_hand)
  while current_score > 21 and number_of_aces > 0:
    current_score -= 10
    number_of_aces -= 1
  return current_score

# Prompt for game:
play_game = play_another_game()
is_game_over = False

while play_game:
  
  print(logo)
  
  (computer_cards, player_cards) = deal_inital_hand()
  user_score = calc_score(player_cards)
  computer_score = calc_score(computer_cards)

  
  # print hands
  print(f"    Your cards: {player_cards}, current score: {calc_score(player_cards)}")
  print(f"    Computer's first card: {computer_cards[0]}")
  
  if user_score == 0 or computer_score == 0:
    is_game_over = True 
  else:
  # prompt hit
  
    hit = True
    while hit and not is_game_over:
      
      hit = to_hit()
      
      if hit:
        #draw
        player_cards += draw_card()
        print(f"    Your cards: {player_cards}, current score: {calc_score(player_cards)}")
      # check score
      if calc_score(player_cards) > 21:
        is_game_over = True
        
    if is_game_over:
      
      print("L-O-S-E-R")
    else:
      
      computer_cards = resolve_dealer_hand(computer_cards)
      if calc_score(computer_cards) > 21:
        
        print("winnner winner chicken dinner")
      else:
        
        if calc_score(player_cards) > calc_score(computer_cards):
          
          print("winner")
        else: 
          print("loser")
          
  # prompt additional game.
  play_game = play_another_game()
  
  
# -[x] Play order:
# -[x] Dealr draws 1
# -[x] Player draws 2
# -[x] Players hit
# -[x] Dealer finishes drawing
# -[x] Bets are settled. 