import prompt
from random import choice, randint
from brain_games import cli


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
        print('Question: ' + str(random_number1) + ' ' + char + ' ' + str(random_number2))
        answer = prompt.string('Your answer: ')
        if char == '*':
            question = random_number1 * random_number2            
        elif char == '+':
            question = random_number1 + random_number2  
        elif char == '-':
            question = random_number1 - random_number2 
        if str(answer) == str(question):
            print('Correct!')
        else:
            print("'" + str(answer) + "'" + " is wrong answer ;(. Correct answer was " +  "'" + str(question) + "'.")
            return "Let's try again, " + cli.name
        i += 1
    return 'Congratulations, ' + cli.name + '!'
