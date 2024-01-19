from random import randint, choice
from operator import add, sub, mul

RULES_CALC = 'What is the result of the expression?'


def game_data():
    # Генерация случайных чисел
    roll_number_one = randint(1, 100)
    roll_number_two = randint(1, 100)

    # Список операторов
    expression_operators = ['+', '-', '*']

    # Выбор случайного оператора
    operator_choice = choice(expression_operators)

    # Создание выражения и вычисление строки, как кода.
    computer_question = f'{roll_number_one} {operator_choice} {roll_number_two}'
    if operator_choice == '+':
        result_game = add(roll_number_one, roll_number_two)
    elif operator_choice == '-':
        result_game = sub(roll_number_one, roll_number_two)
    elif operator_choice == '*':
        result_game = mul(roll_number_one, roll_number_two)
    return computer_question, result_game
