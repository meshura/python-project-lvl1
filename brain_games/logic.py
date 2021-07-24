def logic(answer, question):
    if str(answer) == str(question):
        return 'Correct!'
    else:
        print("'" + str(answer) + "'" + " is wrong answer ;(. Correct answer was " +  "'" + str(question) + "'.")
        return None
