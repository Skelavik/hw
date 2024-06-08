
import requests
import random
import basic_word
def load_random_word():

    file_data = requests.get("https://www.jsonkeeper.com/b/ILQO")
    data = file_data.json()
    random.shuffle(data)
    x = random.randint(0, 2)
    return basic_word.BasicWord(data[x]["words"], data[x]["subwords"])