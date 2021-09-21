#game.py
import random
print ("Rock, Paper, Scissors, Shoot!")

user_choice = input("choose 'Rock' or 'Paper' or 'Scissors':")
print("User Chose:")
print(user_choice)

options = ["Rock","Paper","Scissors"]

computer_choice = random.choice(options)
print("Computer Chose:")
print(computer_choice)

