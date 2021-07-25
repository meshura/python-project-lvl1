import prompt
from random import choice, randint
from brain_games import cli
from brain_games import logic


def game_2():
    cli.hello()
    print("Hello, " + cli.name + "!")
    print('What is the result of the expression?')
    i = 0
    while i < 3:
        random_number1 = randint(1, 100)
        random_number2 = randint(1, 100)
        string = '*+-'
        char = choice(string)
        exam = "Question: {} {} {}"
        print(exam.format(str(random_number1), str(char), str(random_number2)))
        answer = prompt.string('Your answer: ')
        if char == '*':
            question = random_number1 * random_number2
        elif char == '+':
            question = random_number1 + random_number2
        elif char == '-':
            question = random_number1 - random_number2
        if logic.logic(answer, question) is None:
            return "Let's try again, " + cli.name + "!"
        i += 1
    return 'Congratulations, ' + cli.name + '!'
