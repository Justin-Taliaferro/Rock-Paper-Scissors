#game.py
import random

import os
from dotenv import load_dotenv

load_dotenv()

x = os.getenv("PLAYER_NAME", default= "Player One")
print("Welcome ",x," to my Rock-Paper-Scissors Game")

# adapted code from Dominic Parente
user_choice = input("choose 'Rock' or 'Paper' or 'Scissors':")
if user_choice in ["Rock", "Paper", "Scissors"]:
    print("User Chose:")
    print(user_choice)
else:
    print("Your choice is invalid, try typing something else!")
    print("Try Again")
    exit()

options = ["Rock","Paper","Scissors"]

computer_choice = random.choice(options)
print("Computer Chose:")
print(computer_choice)
if computer_choice == user_choice:
    print("You chose the same option, please pick again")
elif user_choice == "rock":
    if computer_choice == "scissors":
        print ("Rock smashes scissors, congrats you won")
    else:
        print ("Paper covers rock, sorry you lost")
elif user_choice == "scissors":
    if computer_choice == "rock":
        print ("Rock smashes scissors, sorry you lost")
    else:
        print ("Scissors cuts paper, congrats you won")
elif user_choice == "paper":
    if computer_choice == "rock":
        print("Paper covers rock, congrats you won") 
    else:
        print("Scissors cuts paper, sorry you lost")
        

