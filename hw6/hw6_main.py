import random

import hw6_get_word

word = hw6_get_word.get_word()

def random_abc_in_word(word):
    word_ = list(word)
    random.shuffle(word_)
    word_code = ('').join(word_)
    return word_code

def answer_output_in_file(user_name,count_point_user):
    with open("history.txt","a",encoding="UTF8") as f:
        f.write(user_name)
        f.write(' ')
        f.write(str(count_point_user))
        f.write("\n")
    return 0

def print_point():
    with open("history.txt", encoding="UTF8") as f:
        for user_point in f:
            print(user_point)
    return 0

user_name = input("Ваше имя: ")
count_point_user = 0

while True:
    word = hw6_get_word.get_word()
    print("Угадайте слово")
    word_abc = random_abc_in_word(word)
    print(word_abc)
    user_answer = input("Ответ: ")
    if user_answer == (""
                       ""):
        break
    #print(user_answer,word)
    if user_answer == word:
        print("Верно +10 очков")
        count_point_user += 10
    else:
        print("Жаль")
        print(f"Правильно {word}")


print(f"Вот и все {user_name}) Ты набрал {count_point_user} очков")
answer_output_in_file(user_name, count_point_user)

print_point()

