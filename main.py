from replit import clear
from art import logo

print(logo)

game_on = True

dict_main = {}

while game_on:
    name = input("What is your name?:")
    bid = input("What is your bid?: $")
    dict_main[name] = bid
    print(dict_main)
