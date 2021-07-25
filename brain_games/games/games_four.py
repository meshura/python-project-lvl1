import prompt
from random import randint
from brain_games import cli
from brain_games import logic


def game_4():
    cli.hello()
    print("Hello, " + cli.name + "!")
    print('What number is missing in the progression?')
    i = 0
    while i < 3:
        start_prog = randint(1, 20)
        increase_prog = randint(1, 10)
        stop_prog = start_prog + (10 * increase_prog)
        shadow_number = randint(0, 9)
        prog = list(range(start_prog, stop_prog, increase_prog))
        question = prog.pop(shadow_number)
        prog.insert(shadow_number, '..')
        exam = "Question: {}"
        print(exam.format(str(prog)))
        answer = prompt.string('Your answer: ')
        if logic.logic(answer, question) is None:
            return "Let's try again, " + cli.name + "!"
        i += 1
    return 'Congratulations, ' + cli.name + '!'
