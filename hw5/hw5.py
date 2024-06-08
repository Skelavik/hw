import random

abc_morse = {'a': '.-', 'b': '-...', 'c': '-.-.', 'd': '-..', 'e': '.', 'f': '..-.', 'g': '--.',
            'h': '....', 'i': '..', 'j': '.---', 'k': '-.-', 'l': '.-..', 'm': '--', 'n': '-.', 'o': '---',
            'p': '.--.', 'q': '--.-', 'r': '.-.', 's': '...', 't': '-', 'u': '..-', 'v': '...-', 'w': '.--',
            'x': '-..-', 'y': '-.--', 'z': '--..'}

words = ["dog","cat","car"]
answer = []
def morse_encode(sentence):
    translate_word = []
    for i in range(0,len(sentence)):
        for key,value in abc_morse.items():
            if key == sentence[i]:
                translate_word.append(value)
    ready_word = ('').join(translate_word)
    print(ready_word)
    return ready_word

def get_word():
    word = random.choice(words)
    return word

def print_statistics(answer):
    count_true = 0
    count_false = 0
    for i in range(0,len(answer)):
        if answer[i] == True:
            count_true += 1
        else:
            count_false += 1
    print(f"Всего слов {len(words)}")
    print(f"Правильно отвечено {count_true}")
    print(f"Ошибся в {count_false} ")
    return 0


print("Начнем")
for x in range(0,len(words)):
    word = get_word()
    morse_encode(word)
    if input("Перевод: ") == word:
        print("Красава")
        answer.append(True)
    else:
        print(f"Жаль это не так. Это {word}")
        answer.append(False)


print_statistics(answer)
