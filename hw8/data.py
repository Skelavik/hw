import json
import random

def input_data():
    file = open("data_play.json","r")
    data = json.load(file)
    file.close()
    return data

def random_question(data):
    random.shuffle(data)
    return data




