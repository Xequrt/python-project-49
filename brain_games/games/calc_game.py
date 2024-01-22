from random import randint, choice
from operator import add, sub, mul

RULES_CALC = 'What is the result of the expression?'


def get_game_data():
    # Генерация случайных чисел
    roll_number_one = randint(1, 100)
    roll_number_two = randint(1, 100)

    # Список кортежей пакета operator
    operators = [('+', add), ('-', sub), ('*', mul)]

    # Выбор случайного оператора
    operator, method = choice(operators)

    # Создание выражения и вычисление выражения.
    computer_question = f'{roll_number_one} {operator} {roll_number_two}'
    result_game = method(roll_number_one, roll_number_two)

    return computer_question, result_game
