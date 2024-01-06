#!/usr/bin/env python3

import prompt


GAME_ATTEMPT = 3

def run_game(rules, game_data):
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print(f"Hello, {name}!")
    game_round = 1
    print(rules)
    while game_round <= GAME_ATTEMPT:
        computer_question, result_game = game_data()
        print(f'Question: {computer_question}')
        user_answer = prompt.string('Your answer: ')
        if result_game == user_answer.lower():
            print('Correct!')
        elif result_game != user_answer.lower() and user_answer.lower() == 'no':
            print(f''''no' is wrong answer ;(. Correct answer was 'yes'.
Let's try again, {name}!''')
            break
        elif result_game != user_answer.lower() and user_answer.lower() == 'yes':
            print(f''''yes' is wrong answer ;(. Correct answer was 'no'.
Let's try again, {name}!''')
            break
        else:
            print(f'"{user_answer}" is wrong answer ;(. Correct answer only "yes" or "no"')
            break
        if game_round == GAME_ATTEMPT:
            print(f'Congratulations, {name}!')
        game_round += 1

