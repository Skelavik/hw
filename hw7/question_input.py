import json
count_question = 0

def get_question():                                         #Импортируем вопросы
    question = open("data.json",encoding="UTF8")
    question = json.load(question)
    return question

def show_field(question):                                   #Печатаем игровое поле
    for name_catergory, point in question.items():
        print(name_catergory.ljust(12), end="")
        for point_word, info in point.items():
            if info["asked"] == False:
                print(point_word.ljust(5), end="")
            else:
                print("".ljust(5), end="")

        print()

question = get_question()





