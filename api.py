import requests
def get_question():
    url = 'https://opentdb.com/api.php?amount=1'
    response = requests.get(url)
    data = response.json()
    question = data['results'][0]['question']
    print(f'{question}')
    answer = input('Your answer:\n')
    correct_answer = data['results'][0]['correct_answer']
    return question, correct_answer