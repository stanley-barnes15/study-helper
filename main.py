from api import get_question, get_user_category
questions, correct_answers = get_question(get_user_category())
for question, correct_answer in zip(questions, correct_answers):
    print(question)
    answer = input('Your answer: ')
    if answer.lower() == correct_answer.lower():
        print('Correct!')
    else:
        print(f'Wrong! The correct answer is: {correct_answer}')