# Задача 32: Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону
#  (т.е. не меньше заданного минимума и не больше заданного максимума)


lst = [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
min_number = int(input("Введите минимальное значение: "))
max_number = int(input("Введите максимальное значение: "))
indexes = []

for i in range(len(lst)):
    if lst[i] >= min_number and lst[i] <= max_number:
        indexes.append(i)

print("Индексы элементов массива, значения которых находятся в диапазоне от {} до {}: {}".format(min_number, max_number, indexes))
