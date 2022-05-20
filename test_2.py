with open("base\\words.txt", "r", encoding="utf-8") as file:
    words_array = [row.strip('\n') for row in file]

print(f"Слов в словаре: {len(words_array)}")
word = input("Введите слово: ")
print("Составь маску поиска. (+) - буква на месте, (=) - буква правильная, но не на месте, (-) - такой буквы нет.")
mask = input("Маска: ")


def sorted_by_length(array, words_mask):
    new_array = []
    for i in range(0, len(array)):
        if len(array[i]) == len(words_mask):
            new_array.append(array[i])
    return new_array


def alphabetical_sorting(array, words_mask, current_word):
    new_array = []
    for word_in_array in array:  # перебор слов в массиве
        flag_1 = True
        flag_2 = False
        flag_3 = True

        for i in range(len(word_in_array)):  #
            if words_mask[i] == "+":  # буква на месте
                if current_word[i] != word_in_array[i]:  # если буква есть в слове на этом же месте, то
                    flag_1 = False
            elif words_mask[i] == "=":  # буква правильная, но не на месте (не работает)
                for x in range(len(word_in_array)):  # перебор символов в маске
                    if words_mask[x] != "+" and x != i and current_word[x] == word_in_array[i]:  # если данная позиция не буква на месте и не стоит там же
                        flag_2 = True
            elif words_mask[i] == "-":  # такой буквы нет
                if current_word[i] in word_in_array:  # если текущая буква есть в слове
                    flag_3 = False
            else:
                print("Ошибка составления маски!!!")

        if flag_1 and flag_2 and flag_3:
            new_array.append(word_in_array)
    return new_array


sort_array = sorted_by_length(words_array, word)
print(alphabetical_sorting(sort_array, mask, word))
print(len(alphabetical_sorting(sort_array, mask, word)))
