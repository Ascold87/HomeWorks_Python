# 4- Напишите программу, которая будет преобразовывать десятичное число в двоичное. Подумайте, как это можно решить с помощью рекурсии.
# Не использовать функцию bin
# Пример:
# 45 -> 101101
# 3 -> 11
# 2 -> 10

print('Программа преобразовывает десятичное число в двоичное.')
import random

num_a = random.randint(0, 999)
num_b = num_a
num_c = ''
while num_b > 0:
    num_c = str(num_b % 2) + num_c
    num_b = num_b // 2
print(f"Десятичное число {num_a}, в двоичной системе соответствует - {num_c}")

