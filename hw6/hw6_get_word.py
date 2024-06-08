
import random
def get_word():
    with open("words.txt","r",encoding="UTF8") as file:
        line = file.read()
        words = line.split()
    random.shuffle(words)
    return words[0]





