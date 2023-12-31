#!/usr/bin/env python3

from brain_games.body_game.body_game import run_game
from random import randint

RULES_EVEN = 'Answer "yes" if the number is even, otherwise answer "no".Answer "yes" if the number is even, otherwise answer "no".'

def game_data():
    roll_number = randint(1, 100)
    computer_question = f'{roll_number}'
    if even_check(roll_number) == True:
        result_game: str = "yes"
    else:
        result_game: str = "no"
    return computer_question, result_game

def even_check(roll_number):
    return True if roll_number % 2 == 0 else False