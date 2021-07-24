import prompt


def welcome_user():
    print('Welcome to the Brain Games!!')
    global name
    name = prompt.string('May I have your name? ')
    return name


def hello():
    return ("Hello, " + welcome_user() + "!")
