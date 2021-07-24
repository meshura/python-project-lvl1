def logic(answer, question):
    if str(answer) == str(question):
        return 'Correct!'
    else:
        bad_answer = "'{}' is wrong answer ;(. Correct answer was '{}'."
        print(bad_answer.format(str(answer), str(question)))
        return None
