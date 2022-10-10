with open("base\\words.txt", "r", encoding="utf-8") as file:
    words_array = [row.strip('\n') for row in file]
print(f"Слов в словаре: {len(words_array)}")
word_counter = 0


def filter_by_length(array, words_mask):
    """Фильтрует массив по количеству букв в исходном слове"""
    new_array = []
    for i in range(0, len(array)):
        if len(array[i]) == len(words_mask):
            new_array.append(array[i])
    return new_array


def filter_wrong_letter(array, words_mask, current_word):
    """Фильтрует по буквам которых нет в слове"""
    filter_array = []
    for word in array:
        flag = True
        for i in range(len(word)):
            if words_mask[i] == "-" and current_word[i] in word:
                flag = False
        if flag:
            filter_array.append(word)
    return filter_array


def filter_right_letter(array, words_mask, current_word):
    """Фильтрует по правильной букве"""
    filter_array = []
    for word in array:
        flag = True
        for i in range(len(word)):
            if words_mask[i] == "+":
                if word[i] != current_word[i]:
                    flag = False
        if flag:
            filter_array.append(word)
    return filter_array


def filter_include_letter(array, words_mask, current_word):
    """Фильтрует по букве которая есть в слове"""
    filter_array = []
    for word in array:
        flag_1 = True
        for i in range(len(words_mask)):
            if words_mask[i] == "=":
                if current_word[i] not in word:
                    flag_1 = False
                elif current_word[i] == word[i]:
                    flag_1 = False
        if flag_1:
            filter_array.append(word)
    return filter_array


while word_counter != 1:
    word = input("Введите слово: ")
    print("Составь маску. (+) - буква на месте, (=) - буква правильная, но не на месте, (-) - такой буквы нет.")
    mask = input("Маска: ")
    if word_counter == 0:
        sort_array = filter_by_length(words_array, word)
    sort_array = filter_wrong_letter(sort_array, mask, word)
    sort_array = filter_right_letter(sort_array, mask, word)
    sort_array = filter_include_letter(sort_array, mask, word)
    print(f"Подходящих слов: {len(sort_array)}")
    word_counter = len(sort_array)
    if word_counter != 1:
        print(sort_array)

print(f"Слово найдено: {sort_array[0]}")
