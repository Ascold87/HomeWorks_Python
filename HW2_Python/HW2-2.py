# 2 - Напишите программу, которая принимает на вход число N и выдает набор произведений (набор - это список) чисел от 1 до N.
# Не используйте функцию math.factorial.
# Пример:
# - пусть N = 4, тогда [ 1, 2, 6, 24 ]
# (1, 1*2, 1*2*3, 1*2*3*4)

print('Программа выдает список произведений чисел от 1 до введенного (факториал).')

num_in = int(input("Введите число: "))
num_result = []

def factorial(n):
    if n != 1:
        return n * factorial(n - 1)
    else:
        return 1

for i in range(1, num_in + 1):
    num_result.append(factorial(i))

print(num_result)