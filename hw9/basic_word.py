class BasicWord:
    def __init__(self, base_word, set_answer):
        self.base_word = base_word
        self.set_answer = set_answer

    def check_in_input_set(self, user_answer):
        if user_answer in self.set_answer:
            return True
        else:
            return False

    def count_word_in_set(self):
        return int(len(self.set_answer))

    def __repr__(self):
        return self.base_word