import requests
import html
def get_question(category, type, difficulty):
    questions = []
    correct_answers = []
    incorrect_answers = []
    params = {"amount": 10}
    url = 'https://opentdb.com/api.php'
    if category != 0:
        params["category"] = category
    if difficulty != "any":
        params["difficulty"] = difficulty
    if type != "any":
        params["type"] = type
    response = requests.get(url,params=params)
    data = response.json()
    while data['response_code'] != 0:
        print('Error retrieving questions. Please choose again.')
        category = get_user_choices()
        if category != 0:
            params["category"] = category
        if difficulty != "any":
            params["difficulty"] = difficulty
        if type != "any":
            params["type"] = type
        response = requests.get(url,params=params)
        data = response.json()
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

def get_user_choices():
    type = input('Please enter the type of questions you want to play (multiple/boolean/any):\n')
    while type not in ['multiple', 'boolean', 'any']:
        type = input('Invalid question type. Please enter again.\n')
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
        return get_user_choices()
    difficulty = input('Please enter the difficulty level you want to play (easy/medium/hard/any):\n')
    while difficulty not in ['easy', 'medium', 'hard', 'any']:
        difficulty = input('Invalid difficulty level. Please enter again.\n')
    return category, type, difficulty