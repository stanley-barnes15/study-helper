import requests
import html
def get_question(category, type, difficulty):
    questions = []
    correct_answers = []
    incorrect_answers = []
    if type == 'any':
        if category == '0':
            if difficulty == 'any':
                url = 'https://opentdb.com/api.php?amount=10'
            else:
                url = f'https://opentdb.com/api.php?amount=10&difficulty={difficulty}'
        else:
            if difficulty == 'any':
                url = f'https://opentdb.com/api.php?amount=10&category={category}'
            else:
                url = f'https://opentdb.com/api.php?amount=10&category={category}&difficulty={difficulty}'
    else:
        if category == '0':
            if difficulty == 'any':
                url = f'https://opentdb.com/api.php?amount=10&type={type}'
            else:
                url = f'https://opentdb.com/api.php?amount=10&type={type}&difficulty={difficulty}'
        else:
            if difficulty == 'any':
                url = f'https://opentdb.com/api.php?amount=10&category={category}&type={type}'
            else:
                url = f'https://opentdb.com/api.php?amount=10&category={category}&type={type}&difficulty={difficulty}'
    response = requests.get(url)
    data = response.json()
    while data['response_code'] != 0:
        print('Error retrieving questions. Please choose category again.')
        category = get_user_category()
        if type == 'any':
            if category == '0':
                if difficulty == 'any':
                    url = 'https://opentdb.com/api.php?amount=10'
                else:
                    url = f'https://opentdb.com/api.php?amount=10&difficulty={difficulty}'
            else:
                if difficulty == 'any':
                    url = f'https://opentdb.com/api.php?amount=10&category={category}'
                else:
                    url = f'https://opentdb.com/api.php?amount=10&category={category}&difficulty={difficulty}'
        else:
            if category == '0':
                if difficulty == 'any':
                    url = f'https://opentdb.com/api.php?amount=10&type={type}'
                else:
                    url = f'https://opentdb.com/api.php?amount=10&type={type}&difficulty={difficulty}'
            else:
                if difficulty == 'any':
                    url = f'https://opentdb.com/api.php?amount=10&category={category}&type={type}'
                else:
                    url = f'https://opentdb.com/api.php?amount=10&category={category}&type={type}&difficulty={difficulty}'
        response = requests.get(url)
        data = response.json()
    for i in range(10):
        incorrect = []
        question = html.unescape(data['results'][i]['question'])
        correct_answer = html.unescape(data['results'][i]['correct_answer'])
        for j in range(len(data['results'][i]['incorrect_answers'])):
            incorrect.append(html.unescape(data['results'][i]['incorrect_answers'][j]))
        questions.append(question)
        correct_answers.append(correct_answer)
        incorrect_answers.append(incorrect)
    return questions, correct_answers, incorrect_answers

def get_user_category():
    url = 'https://opentdb.com/api_category.php'
    response = requests.get(url)
    data = response.json()
    for name in data['trivia_categories']:
        print(f"{name['id']} - {name['name']}")
    try:
        category = int(input('Please enter the category id you want to play:\n'))
        while str(category) not in [str(name['id']) for name in data['trivia_categories']] and category != 0:
            category = input('Invalid category id.\nPlease enter a valid category id:\n')
    except:
        print('Invalid input. Please enter a number.')
        return get_user_category()
    return category