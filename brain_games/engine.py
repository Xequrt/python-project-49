#!/usr/bin/env python3

import prompt

GAME_ATTEMPT = 3


def run_game(rules, get_game_data):
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print(f"Hello, {name}!")
    print(rules)
    for i in range(GAME_ATTEMPT):
        computer_question, result_game = get_game_data()
        print(f'Question: {computer_question}')
        user_answer = prompt.string('Your answer: ')
        if str(result_game) != user_answer.lower():
            print(f"'{user_answer}' is wrong answer ;(. "
                  f"Correct answer was '{result_game}'\n"
                  f"Let's try again, '{name}!'")
            break
        print('Correct!')
    else:
        print(f'Congratulations, {name}!')
