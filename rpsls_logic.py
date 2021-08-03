import random
from rpsls_dictionaries import *

def get_computer_choice():
    choices = ["Rock", "Paper", "Scissors", "Lizard", "Spock"]
    computer = random.choice(choices)
    return computer

def get_winner(user_choice, computer_choice):
    winner = user_choice + computer_choice
    if winner in rpsls_winner_player:
        winner = "Player beats Computer"
    else:
        winner = "Computer beats Player"
    return winner

def get_message(user_choice, computer_choice):
    key = user_choice + computer_choice
    if key in rpsls_winner_player:
        message = rpsls_winner_player.get(key)
    else:
        message = rpsls_winner_computer.get(key)
    return message

def get_images(user_choice, computer_choice):
    key = user_choice + computer_choice
   
    if key in rpsls_winner_player:
        index = rpsls_images.get(user_choice)
    else:
        index = rpsls_images.get(computer_choice)
    return index