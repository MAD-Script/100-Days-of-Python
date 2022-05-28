# from replit import clear
# #HINT: You can call clear() to clear the output in the console.

import os
from Blind_Auction_art import logo

def clear():
    os.system('cls')

bid = {}

bidding = True

print(logo)
print("Welcome to the secret auction program.")

while(bidding):
    bidder = input("What is your name?: ")
    bid_amount = int(input("What's your bid?:$ "))
    
    bid[bidder] = bid_amount
    
    cont = input("Are there any other bidders? Type 'yes' or 'no'. \n").lower()
    clear()
    if cont == "no":
        bidding = False

highest_bid = 0;

for bidder in bid:
    bid_amount = bid[bidder]

    if bid_amount > highest_bid:
        highest_bid = bid_amount
        highest_bidder = bidder
        
        
print(f"The winner is {highest_bidder} with a bid of ${highest_bid}.")