import utils
import player
using_words = []


#name_player = input("Введите имя игрока: ")
name_player = "eva"
user = player.Player(name_player,using_words)
print(f"Привет {name_player}")
print("Слова не должны быть короче 3 букв")
print("Чтобы закончить напиши 'стоп' ")
print("")

print("Твое слово:")
word = utils.load_random_word()
print(word)

while user.get_count_using_word() != word.count_word_in_set():

    user_answer = input()

    if len(user_answer) < 3:
        print("Короткое слово")
        continue

    if user_answer == "стоп":
        break

    if user_answer not in word.set_answer:
        print("Нет такого слова")
        continue

    if user.check_availability_in_using_word(user_answer) == True:
        print("Это слово уже было")
        continue


    user.add_word_in_using_word(user_answer)
    print("Верно")

print(f"Игра закончена, вы угадали {user.get_count_using_word()} слов")
