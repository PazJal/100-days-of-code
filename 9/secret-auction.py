from art import logo
import os

print(logo)
print("Welcome to the secret auction program.")
bid_again = True

bids = {}


def get_new_bid():
  name = input("What is your name?: ")
  bid = int(input("What's your bid?: $"))
  
  bids[name] = bid
  

while bid_again:
  get_new_bid()
  os.system('cls')
  additional_bidders = input("Are there any other bidders? Type 'yes' or 'no'. \n")
  if additional_bidders == "no":
    bid_again = False
    
winner = max(bids, key=bids.get)
print(f"The winner is {winner} with a bid of ${bids[winner]}")



