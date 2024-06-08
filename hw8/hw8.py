import data

class Question:

    def __init__(self,text_q,level_q,true_answer_q,get_q = False,answer_user = None,point_q = None):
        self.text_q = text_q
        self.level_q = level_q
        self.true_answer = true_answer_q

        self.get_q = get_q
        self.answer_user = answer_user
        self.point_q = point_q

    def get_point(self):
        self.point_q = int(self.level_q) * int(10)
        return self.point_q

    def is_correct(self):
        if self.answer_user == self.true_answer:
            return True
        else:
            return False

    def build_question(self):
        print(self.text_q)
        print(f"Сложность {self.level_q}/5")



    def build_positive_feedback(self):
        return print(f"Ответ верный, плучено {self.point_q} баллов")

    def build_negative_feedback(self):
        return print(f"Ответ неверный, вырный ответ {self.true_answer}")

count_question = 0
point_play = 0
x = 0
data_question = data.input_data()
data.random_question(data_question)

try:
    while True:
        hero = Question(data_question[x]["q"],data_question[x]["d"],data_question[x]["a"])
        hero.get_point()
        hero.build_question()
        hero.answer_user = input("Ответ: ")
        x += 1
        if hero.is_correct() == True:
            hero.build_positive_feedback()
            count_question += 1
            point_play += hero.point_q
        else:
            hero.build_negative_feedback()
        print()
except:
    print("Все")
    print(f"Отвечено {count_question} вопросов из 5")
    print(f"Набрано баллов: {point_play}")

