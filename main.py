from api import get_question, get_user_category
questions, correct_answers, incorrect_answers = get_question(get_user_category())
total = 0
for question, correct_answer, incorrect_answer in zip(questions, correct_answers, incorrect_answers):
    print(f'{question}?')
    incorrect_answer.append(correct_answer)
    for i, option in enumerate(sorted(incorrect_answer)):
       print(f'{i+1}. {option}')
    answer = input('Your answer: ')
    if answer.lower() == correct_answer.lower():
        print('Correct!')
        total += 1
    else:
        print(f'Wrong! The correct answer is {correct_answer}')
print(f'Your total score is {total}/10')