# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример: для k=8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

import random
a = random.randint(3, 10)
b = [1, 1]
for i in range(2, a):
    b.append(b[i-2] + b[i-1])
print(b)
for i in range(len(b)+1):
    b.insert(0, b[1] - b[0])
print(b)