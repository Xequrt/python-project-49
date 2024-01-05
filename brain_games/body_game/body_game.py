#!/usr/bin/env python3

import prompt

from brain_games.games.even_game import game_data

GAME_ATTEMPT = 3

def run_game():
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print(f"Hello, {name}!")
    game_round = 1
    while game_round <= GAME_ATTEMPT:
        computer_question, result_game = game_data()
        print(f'Question: {computer_question}')
        user_answer = prompt.string('Your answer: ')
        if result_game == user_answer.lower():
            print('Correct!')
        else:
            print(f''''yes' is wrong answer ;(. Correct answer was 'no'.
Let's try again, {name}!''')
        if game_round == GAME_ATTEMPT:
            print(f'Congratulations, {name}')
        game_round += 1

