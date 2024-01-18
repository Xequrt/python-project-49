from random import randint

RULES_PRIME = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def game_data():
    # Генерация простого числа
    computer_question = randint(1, 100)
    if prime_check(computer_question):
        result_game: str = "yes"
    else:
        result_game: str = "no"
    return computer_question, result_game


def prime_check(computer_question):
    # Проверка числа на простоту
    if computer_question < 2:
        return False
    for i in range(2, int(computer_question ** 0.5) + 1):
        if computer_question % i == 0:
            return False
    return True
