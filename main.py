from api import get_question, get_user_category
questions, correct_answers, incorrect_answers = get_question(get_user_category())

for question, correct_answer, incorrect_answer in zip(questions, correct_answers, incorrect_answers):
    print(f'{question}?')
    incorrect_answer.append(correct_answer)
    for option in sorted(incorrect_answer):
       print(option)
    answer = input('Your answer: ')
    if answer.lower() == correct_answer.lower():
        print('Correct!')
    else:
        print(f'Wrong! The correct answer is {correct_answer}')