import requests
import html
def get_question(category):
    questions = []
    correct_answers = []
    url = f'https://opentdb.com/api.php?amount=10&category={category}'
    response = requests.get(url)
    data = response.json()
    while data['response_code'] != 0:
        print('Error with retrieving questions. Please choose category again.')
        category = get_user_category()
        url = f'https://opentdb.com/api.php?amount=10&category={category}'
        response = requests.get(url)
        data = response.json()
    for i in range(10):
        question = html.unescape(data['results'][i]['question'])
        correct_answer = html.unescape(data['results'][i]['correct_answer'])
        questions.append(question)
        correct_answers.append(correct_answer)
    return questions, correct_answers

def get_user_category():
    url = 'https://opentdb.com/api_category.php'
    response = requests.get(url)
    data = response.json()
    print(data)
    for name in data['trivia_categories']:
        print(f"{name['id']} - {name['name']}")
    try:
        category = int(input('Please enter the category id you want to play:\n'))
        while str(category) not in [str(name['id']) for name in data['trivia_categories']]:
            category = input('Invalid category id.\nPlease enter a valid category id:\n')
    except:
        print('Invalid input. Please enter a number.')
        return get_user_category()
    return category