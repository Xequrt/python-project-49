from random import randint

RULES_PROGRESSION = 'What number is missing in the progression?'

def game_data():
    computer_question = []
    i = 0
    # Генерация первого элемента и разности прогрессии
    roll_an = randint(1, 20)
    roll_d = randint(1, 5)

    # Генерация арифметической прогрессии в список
    for i in range(10):
        computer_question.append(roll_an + roll_d)
        roll_an += roll_d

    # Генерация случайного индекса
    index = randint(0, len(computer_question) - 1)
    result_game = computer_question[index]
    computer_question[index] = ".."

    return computer_question, result_game