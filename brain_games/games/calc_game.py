import random
from random import randint, choice

RULES_CALC = 'What is the result of the expression?'

def game_data():
    # Список операторов
    expression_operators = ['+', '-', '*']

    # Генерация случайных чисел и операторов
    roll_number_one = randint(1, 100)
    roll_number_two = randint(1, 100)
    operator_choice = random.choice(expression_operators)

    # Создание выражения и вычисление строки, как кода.
    computer_question = f'{roll_number_one}{operator_choice}{roll_number_two}'
    result_game = str(eval(computer_question))
    return computer_question, result_game