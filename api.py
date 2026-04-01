import requests
import html
def get_question(category):
    url = f'https://opentdb.com/api.php?amount=10&category={category}&type=boolean'
    response = requests.get(url)
    data = response.json()
    question = data['results'][0]['question']
    question = html.unescape(question)
    print(f'True or False, {question}?')
    correct_answer = data['results'][0]['correct_answer']
    correct_answer = html.unescape(correct_answer)
    return question, correct_answer

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