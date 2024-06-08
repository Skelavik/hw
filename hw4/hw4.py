easy = {"cat":"кот","dog":"собака"}
medium = {"car":"машина","train":"поезд"}

levels = {1:"первый",2:"второй"}
answer = {}
words = {}

level_selection = input("Выбирите уровень(1, 2): ")
level = levels.get(int(level_selection))
if level == "первый":
    words = easy
elif level == "второй":
    words = medium

for key,value in words.items():
    print(f"Слово: {key}. Длина слова {len(value)} Первая буква: {value[0]}:")
    user_answer = input("Ответ: ")

    if user_answer == value:
        answer[value] = True
    else:
        answer[value] = False

print("Правильно ответил:")
for key,value in answer.items():
    if value == True:
        print(key)

print("Неправильно ответил:")
for key,value in answer.items():
    if value == False:
        print(key)



