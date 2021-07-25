import prompt
from random import randint
from brain_games import cli
from brain_games import logic


def game5_logic(number1_1):
    var = []
    for index in range(number1_1):
        if index == 0:
            continue
        if number1_1 % index == 0:
            var.append(index)
    if len(var) == 1:
        return 'yes'
    else:
        return 'no'


def game_5():
    cli.hello()
    print("Hello, " + cli.name + "!")
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    i = 0
    while i < 3:
        number = randint(1, 3571)
        question = game5_logic(number)
        exam = "Question: {}"
        print(exam.format(str(number)))
        answer = prompt.string('Your answer: ')
        if logic.logic(answer, question) is None:
            return "Let's try again, " + cli.name + "!"
        i += 1
    return 'Congratulations, ' + cli.name + '!'
