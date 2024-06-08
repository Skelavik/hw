import question_input
import json

points = 0
correct = 0
incorrect = 0

def parse_input():                                          #Что написал user разеляем
    user_input = input()
    user_category_point = user_input.split(' ')
    return user_category_point

def show_question(question,user_input):                     #Печатаем вопрос
    for name_category,point in question.items():
        for point_word,info in point.items():
            if name_category == user_input[0] and point_word == user_input[1]:
                print(f"Слово {info['question']} в переводе означает: ", end="")
                return info,point_word

def show_status(points,correct,incorrect):
    results_play = {"points":" " ,"correct":" ", "incorrect":" "}
    results_play["points"] = points
    results_play["correct"] = correct
    results_play["incorrect"] = incorrect
    print(f"Ваш счет: {points} \n"
          f"Верных ответов: {correct} \n"
          f"Неверных ответов: {incorrect} \n")
    return results_play

def save_results_to_file(results_play):

    file = open("results.json","r")
    results = json.load(file)
    results = results_play
    file.close()

    file = open("results.json","w")
    json.dump(results, file)
    file.close()



try:
    while True:

        question = question_input.question                              #Загружаем слова из файла
        question_input.show_field(question)                             #Печатаем поле
        user_input = parse_input()                                      #Разделяем категории
        info, point_word = show_question(question, user_input)

        user_answer = input()

        if user_answer == info['answer']:
            print(f"Верно. Вам +{point_word}")
            points = points + int(point_word)
            correct = correct + 1
        else:
            points = points - int(point_word)
            incorrect = incorrect + 1
            print(f"Неверно. Правильный ответ: {info['answer']}. У вас -{point_word}")


        info['asked'] = True
except:
    print("Вот игра и закончилась. Результаты: ")
    results_play = show_status(points, correct, incorrect)
    save_results_to_file(results_play)
