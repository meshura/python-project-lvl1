import prompt
from random import randint
from brain_games import cli
from brain_games import logic


def game_1():
    cli.hello()
    print("Hello, " + cli.name + "!")
    print('Answer "yes" if the number is even, otherwise answer "no".')
    i = 0
    while i < 3:
        random_number = randint(1, 100)
        print('Question: ', random_number)
        answer = prompt.string('Your answer: ')
        if random_number % 2 == 0:
            question = 'yes'
        elif random_number % 2 > 0:
            question = 'no'
        if logic.logic(answer, question) is None:
            return "Let's try again, " + cli.name
        i += 1
    return 'Congratulations, ' + cli.name + '!'
