answer = ["is","am","in"]

def vopros_1():
    return ("My name ___ Aleks: ")
def vopros_2():
    return ("I ___ a coder: ")
def vopros_3():
    return ("I live ___ Moscow: ")

user = input("Ваше имя")
print(f"{user} начнем игру")

answer_user = input(vopros_1())
if answer_user == answer[0]:
    print("Ответ верный")
else:
    print(f"Неверно ответ {answer[0]}")

answer_user = input(vopros_2())
if answer_user == answer[1]:
    print("Ответ верный")
else:
    print(f"Неверно ответ {answer[1]}")

answer_user = input(vopros_3())
if answer_user == answer[2]:
    print("Ответ верный")
else:
    print(f"Неверно ответ {answer[2]}")


