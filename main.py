from api import get_question
question, correct_answer = get_question()
answer = input('Your answer:\n')
if answer.lower() == correct_answer.lower():
    print('Correct!')
else:
    print(f'Wrong! The correct answer is {correct_answer}.')