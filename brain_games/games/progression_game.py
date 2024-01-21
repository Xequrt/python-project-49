from random import randint

RULES_PROGRESSION = 'What number is missing in the progression?'


def game_data():
    # Генерация первого элемента, разности и длины прогрессии
    roll_an = randint(1, 20)
    roll_d = randint(1, 5)
    roll_len = randint(5, 10)
    # Расчет конца прогрессии
    end_an = roll_d * roll_len + roll_an
    # Генерация арифметической прогрессии в список
    computer_question_list = list(range(roll_an, end_an, roll_d))
    # Генерация случайного индекса
    index = randint(0, roll_len)
    result_game = computer_question_list[index]
    computer_question_list[index] = ".."
    computer_question_str = [str(i) for i in computer_question_list]
    computer_question = ' '.join(computer_question_str)
    return computer_question, result_game
