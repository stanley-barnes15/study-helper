from api import get_question, get_user_category
questions, correct_answers, incorrect_answers = get_question(get_user_category(), input('Please enter the type of questions you want to play (multiple/boolean/any):\n'))
total = 0
for question, correct_answer, answers in zip(questions, correct_answers, incorrect_answers):
    print(f'{question}?')
    answers.append(correct_answer)
    answers = sorted(answers)
    for i, option in enumerate(answers):
       print(f'{i+1}. {option}')
    answer = input('Your answer: ')
    if answer.lower() == correct_answer.lower() or answer == str(answers.index(correct_answer)+1):
        print('Correct!')
        total += 1
    else:
        print(f'Wrong! The correct answer is {correct_answer}')
print(f'Your total score is {total}/10')