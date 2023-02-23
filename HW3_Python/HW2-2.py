# 2 - Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# [2, 3, 4, 5, 6] => [12, 15, 16];
# [2, 3, 5, 6] => [12, 15]

import random
print('Программа, выводит произведение пар цифр массива, начиная с крайних.')

first_array = []
first_length = random.randint(5, 10)
for i in range(first_length):
    k = random.randint(1, 10)
    first_array.append(k)
print(f"Первоначальный набор: {first_array}")

half_length = first_length // 2
y = []
for i in range(half_length):
    y.append(first_array[i] * first_array[(first_length-1)-i])
if len(first_array) % 2 != 0:
    y.append(first_array[half_length]**2)
print(f"Перемноженные пары: {y}")