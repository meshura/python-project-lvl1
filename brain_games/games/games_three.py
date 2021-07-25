import prompt
from random import randint
from brain_games import cli
from brain_games import logic


def game3_logic_2(var1_1, var2_2):
    var3 = []
    if len(var1_1) > len(var2_2):
        var1_1, var2_2 = var2_2, var1_1
    for j in var1_1:
        if j in var2_2:
            var3.append(j)
    return var3


def game3_logic_1(random_number1, random_number2):
    var1 = []
    var2 = []
    for index1 in range(1, random_number1 + 1):
        if random_number1 % index1 == 0:
            var1.append(index1)
    for index2 in range(1, random_number2 + 1):
        if random_number2 % index2 == 0:
            var2.append(index2)
    return max(game3_logic_2(var1, var2))


def game_3():
    cli.hello()
    print("Hello, " + cli.name + "!")
    print('Find the greatest common divisor of given numbers.')
    i = 0
    steps = 3
    while i < steps:
        random_number1_1 = randint(1, 100)
        random_number2_2 = randint(1, 100)
        question = game3_logic_1(random_number1_1, random_number2_2)
        exam = "Question: {} {}"
        print(exam.format(str(random_number1_1), str(random_number2_2)))
        answer = prompt.string('Your answer: ')
        if logic.logic(answer, question) is None:
            return "Let's try again, " + cli.name + "!"
        i += 1
    return 'Congratulations, ' + cli.name + '!'
