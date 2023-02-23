# 5 - Задайте число.
# Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:
# для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

import random
print('Программа показывает список чисел Фибоначчи.')
user_num = random.randint(1, 15)

def fibonachi_minus_to_plus(num: int, list=[]):
    list_1 = []
    f1 = 0
    f2 = 1
    for _ in range(num):
        list_1.append(f1)
        f1, f2 = f2, f1 + f2
    list_1.pop(0)
    list_2 = []
    p1 = 0
    p2 = -1
    for _ in range(0, (-1*num), -1):
        list_2.append((p1)*-1)
        p1, p2 = p2, p1 - p2
    list = list_2[::-1] + list_1
    return print(list)


print('Индекс числа задан системой, как -', user_num)
fibonachi_minus_to_plus(user_num)
