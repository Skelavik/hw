questions = ["My name ___ Vova","I ___ coder","I live ___ Moscow"]
answer = ["is","am","in"]
count_questions = len(questions)
count_point = 0
x = 2

start_user = input("Набирите go чтобы начать: ")

if start_user == "go":
    for i in range(0,3):
        print(questions[i])
        while x > 0:
            if input("Ответ: ") == answer[i]:
                print("Правильно")
                count_point += 1
                break
            else:
                print("Неапрвыильно")
                print(f"Осталось попыток: {x-1}")
                x -= 1
                if x == 0:
                    print(f"Неверно. Правильный ответ: {answer[i]}")

        x = 2
    print(f"Вы ответили на {count_point} вопрососв из {count_questions}.")
    procent = int((count_point)/(count_questions) * 100)
    print(f"Это {procent} процентов")
else:
    print("Жаль")