import prompt
from random import randint
from brain_games import cli


def game_1():
    cli.welcome_user()
    cli.hello()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    i = 0
    while i < 3:
        random_number = randint(1, 100)
        print('Question: ', random_number)
        answer = prompt.string('Your answer: ')
        if random_number % 2 == 0 and answer == 'yes':
            print('Correct!')
        elif random_number % 2 > 0 and answer == 'no':
            print('Correct!')
        else:
            print("'yes' is wrong answer ;(. Correct answer was 'no'.")
            return "Let's try again, " + cli.name
        i += 1
    return 'Congratulations, ' + cli.name + '!'
