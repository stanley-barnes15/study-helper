from api import get_question, get_user_category
question, correct_answer = get_question(get_user_category())
answer = input('Your answer:\n')
if answer.lower() == correct_answer.lower():
    print('Correct!')
else:
    print(f'Wrong! The correct answer is {correct_answer.lower()}.')