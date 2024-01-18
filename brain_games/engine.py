#!/usr/bin/env python3

import prompt

GAME_ATTEMPT = 3


def run_game(rules, game_data):
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print(f"Hello, {name}!")
    print(rules)
    for i in range(3):
        computer_question, result_game = game_data()
        print(f'Question: {computer_question}')
        user_answer = prompt.string('Your answer: ')
        if str(result_game) == user_answer.lower():
            print('Correct!')
        else:
            print(f''''{user_answer}' is wrong answer ;(.
Correct answer was '{result_game}'.
Let's try again, {name}!''')
            break
        if i == GAME_ATTEMPT - 1:
            print(f'Congratulations, {name}!')
