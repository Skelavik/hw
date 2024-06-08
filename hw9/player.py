class Player:
    def __init__(self,name_user,using_words = None):
        self.name_user = name_user
        self.using_words = using_words

    def get_count_using_word(self):
        return int(len(self.using_words))

    def add_word_in_using_word(self, user_answer):
        self.using_words.append(user_answer)

    def check_availability_in_using_word(self,user_answer):
        if user_answer in self.using_words:
            return True
        else:
            return False

    def __repr__(self):
        print(self.name_user)