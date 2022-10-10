import random

players_word = None
attempt = 0

with open("base\\words.txt", "r", encoding="utf-8") as file:
    words_array = [row.strip('\n') for row in file]

print("----- УГАДАЙ СЛОВО -----")
number_letters = int(input("Введи количество букв в слове: "))
print("(+) - буква на месте, (=) - буква правильная, но не на месте, (-) - такой буквы нет.")


def filter_by_length(array, len_words):
    """Фильтрует словарь по количеству букв"""
    new_array = []
    for i in range(0, len(array)):
        if len(array[i]) == len_words:
            new_array.append(array[i])
    return new_array


def check_by_letters(hidden_word, word_player):
    mask = []
    for x in range(len(hidden_word)):
        if hidden_word[x] == word_player[x]:
            mask.append("+")
        elif hidden_word[x] != word_player[x] and not word_player[x] in hidden_word:
            mask.append("-")
        elif hidden_word[x] != word_player[x]:
            mask.append("=")
    return mask


words_array = filter_by_length(words_array, number_letters)
word = words_array[random.randint(0, len(words_array))]
print(word)


while players_word != word:
    attempt += 1
    players_word = input("Введи слово: ")
    if players_word in words_array and len(players_word.strip('\n')) == number_letters:
        if players_word == word:
            check = True
            print(f"Слово '{word}' угадано, за {attempt} попытки!!!")
        else:
            print(check_by_letters(word, players_word))
    else:
        print("Такого слова нет, либо в слове отличное количество букв.")
