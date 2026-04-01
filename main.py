from api import get_question, get_user_category
category = get_user_category()
type = input('Please enter the type of questions you want to play (multiple/boolean/any):\n')
while type not in ['multiple', 'boolean', 'any']:
    type = input('Invalid question type. Please enter again.\n')
difficulty = input('Please enter the difficulty level you want to play (easy/medium/hard/any):\n')
while difficulty not in ['easy', 'medium', 'hard', 'any']:
    difficulty = input('Invalid difficulty level. Please enter again.\n')
questions, correct_answers, incorrect_answers = get_question(category, type, difficulty)
total = 0
for question, correct_answer, answers in zip(questions, correct_answers, incorrect_answers):
    print(question)
    answers.append(correct_answer)
    answers = sorted(answers)
    if len(answers) == 2:
        answers = ['True', 'False']
    for i, option in enumerate(answers):
       print(f'{i+1}. {option}')
    answer = input('Your answer: ')
    if answer.lower() == correct_answer.lower() or answer == str(answers.index(correct_answer)+1):
        print('Correct!')
        total += 1
    else:
        print(f'Wrong! The correct answer is {correct_answer}')
print(f'Your total score is {total}/10')