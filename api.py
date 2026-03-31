import requests
import html
def get_question():
    url = 'https://opentdb.com/api.php?amount=10&category=18&type=boolean'
    response = requests.get(url)
    data = response.json()
    question = data['results'][0]['question']
    question = html.unescape(question)
    print(f'True or False, {question}?')
    correct_answer = data['results'][0]['correct_answer']
    correct_answer = html.unescape(correct_answer)
    return question, correct_answer