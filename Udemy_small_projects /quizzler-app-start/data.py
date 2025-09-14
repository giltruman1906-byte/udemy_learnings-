import requests

def get_questions():
    my_amount = 5
    my_type = "boolean"

    parametres = {
        "amount" : my_amount,
        "type" : my_type
    }
    respond = requests.get(url = "https://opentdb.com/api.php" ,params = parametres)
    respond.raise_for_status()
    raw_data_results = respond.json()["results"]
    dict = {}
    question_list = []
    for raw_data in raw_data_results:
        question = raw_data["question"]
        is_true = raw_data["correct_answer"]
        dict = {"question" : question ,"is true": is_true}
        question_list.append(dict)
    return question_list
    


