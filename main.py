word_count = 0
word = input("Введите слово: ")
print("*" * 60)
print("||", end=" ")

for x in range(len(word)):
    print(word[x], f"- {x + 1}-я позиция || ", end="")
print()
print("*" * 60)

number_coincidence = int(input("Сколько букв совпало и находятся на своих местах?: "))
position_coincidence = [0] * number_coincidence
for i in range(number_coincidence):
    position_coincidence[i] = int(input(f"Позиция {i + 1}-го совпадения: "))

right_all_letter = input("Введи правильные буквы в слове, но не на месте: ")

wrong_all_letter = input("Введи не правильные буквы: ")

print("*" * 60)

while word_count != 1:
    with open("base\\words.txt", "r", encoding="utf-8") as file1:
        word_count = 0
        word_in_base = 0

        for line in file1:
            word_in_base += 1
            if len(line) == len(word) + 1:
                flag_1 = 0
                flag_2 = 0
                flag_3 = 0
                i = 0
                while i < number_coincidence:
                    if str(line[position_coincidence[i] - 1]) == str(word[position_coincidence[i] - 1]):
                        i += 1
                        flag_1 += 1
                    else:
                        break
                if len(list(right_all_letter)) > 0:
                    for n in range(len(list(right_all_letter))):
                        if list(right_all_letter)[n] in line:
                            flag_2 += 1

                if len(list(wrong_all_letter)) > 0:
                    for p in range(len(list(wrong_all_letter))):
                        if list(wrong_all_letter)[p] in line:
                            flag_3 += 1

                if flag_1 == number_coincidence and flag_2 == len(right_all_letter) and flag_3 == 0:
                    print(line.strip())
                    word_count += 1

    print("*" * 60)
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
