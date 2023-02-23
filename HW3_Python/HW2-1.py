# 1 - Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример:
# [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

print('Программа, находит сумму нечётных элементов списка.')

import random
first_array = []
first_length = random.randint(5, 10)
for i in range(first_length):
    k = random.randint(1, 9)
    first_array.append(k)
print('Список элементов: ', first_array)

second_array = []
summ_of_second = 0
for i in range(len(first_array)):
    if i % 2 != 0:
        second_array.append(first_array[i])
print('Список нечетных элементов: ', second_array)

for j in second_array:
    summ_of_second += j
print(f"Сумма нечетных элементов: {summ_of_second}")