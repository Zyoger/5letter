word_count = 0
word = input("Введите слово: ")
print("Введи маску поиска. (+) - буква на месте, (=) - буква правильная, но не на месте, (-) - такой буквы нет.")
mask = input("Маска: ")

while word_count != 1:

    with open("base\\words.txt", "r", encoding="utf-8") as file1:
        word_count = 0
        word_in_base = 0

        for line in file1:
            word_in_base += 1
            if len(line.rstrip('\n')) == len(word):

                flag_1 = True
                flag_2 = False
                flag_3 = True

                for i in range(len(line.strip('\n'))):
                    if mask[i] == "+":  # буква на месте
                        if word[i] != line.strip('\n')[i]:
                            flag_1 = False
                    elif mask[i] == "=":  # буква правильная, но не на месте
                        for x in range(len(line.strip('\n'))):
                            if mask[x] == "=" or "-":
                                if x != i:
                                    if word[x] == line.strip('\n')[i]:
                                        flag_2 = True
                    elif mask[i] == "-":  # такой буквы нет
                        if word[i] in line.strip('\n'):
                            flag_3 = False
                    else:
                        print("Ошибка составления маски!!!")

                if flag_1 and flag_2 and flag_3:
                    print(line.strip())

                    word_count += 1

"""
    print(f"Поиск завершен. Слов в словаре: {word_in_base}. Всего подходящих слов: {word_count}")
    if word_count != 1:
        word = input("Введите слово из списка: ")

        for x in range(len(word)):
            print(word[x], f"- {x + 1}-я позиция || ", end="")
        print()
        print("*" * 60)

        number_coincidence = int(input("Сколько букв совпало и находятся на своих местах?: "))
        position_coincidence = [0] * number_coincidence
        for i in range(number_coincidence):
            position_coincidence[i] = int(input(f"Позиция {i + 1}-го совпадения: "))

        right_all_letter += input("Добавь правильные буквы в слове, но не на месте: ")

        wrong_all_letter += input("Добавь не правильные буквы: ")

print(f"Слово найдено!")
"""