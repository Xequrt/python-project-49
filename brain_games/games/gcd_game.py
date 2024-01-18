from random import randint

RULES_GCD = 'Find the greatest common divisor of given numbers.'


def game_data():
    # Генерация случайных чисел и операторов
    roll_number_one = randint(1, 100)
    roll_number_two = randint(1, 100)

    # Создание пары чисел для нахождения наибольшего общего делителя.
    computer_question = f'{roll_number_one} {roll_number_two}'

    # Нахождения НОД пары целых чисел алгоритмом Евлклида.
    while roll_number_one != 0 and roll_number_two != 0:
        if roll_number_one > roll_number_two:
            roll_number_one = roll_number_one % roll_number_two
        else:
            roll_number_two = roll_number_two % roll_number_one

    result_game = roll_number_one + roll_number_two

    return computer_question, result_game
