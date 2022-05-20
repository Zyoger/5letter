word = input("Введите слово: ")
print("Введи маску поиска. (+) - буква на месте, (=) - буква правильная, но не на месте, (-) - такой буквы нет.")
mask = input("Маска: ")

with open("base\\words.txt", "r", encoding="utf-8") as file:
    array = [row.strip('\n') for row in file]


def sorted_by_length (words_array):
    pass


def alphabetical_sorting (words_array):
    pass


