from replit import clear
from art import logo

print(logo)

game_on = True

dict_main = {}
keys = []
values = []

while game_on:
    name = input("What is your name?:")
    bid = input("What is your bid?: $")
    continue_bid = input("Are there any other bidders? Type 'yes or 'no'.\n")
    dict_main[name] = bid

    if continue_bid == 'yes':
        clear()
    elif continue_bid == 'no':
        for key, value in dict_main.items():
            keys.append(key)
            values.append(value)
        winner_bid = values.max()
        winner_bid_index = winner_bid.index()
        print(winner_bid_index)
