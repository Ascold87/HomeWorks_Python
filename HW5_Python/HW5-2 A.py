# 2-Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021(или сколько вы скажете) конфета. 
# Играют два игрока делая ход друг после друга. 
# Первый ход определяется жеребьёвкой. 
# За один ход можно забрать не более чем 28 (или сколько вы зададите в начале) конфет. 
# Все конфеты оппонента достаются сделавшему последний ход. 
# a) Добавьте игру против бота
# b) Подумайте как наделить бота "интеллектом"
# Если делаете a и b - не нужно создавать отдельных файлов с полностью копированным кодом, лучше выделите в отдельные функции бота и умного бота.

print('Сыграем в игру с конфетами?')

import random
 # вариант с 2мя игроками. 
sweets_table = int(input("У нас есть такое количества конфет: "))
first_player = input("Имя первого сладкоежки: ")
second_player = input("Имя второго сладкоежки: ")
first_count = 0
second_count = 0
turn = random.randint(1, 2)
if turn == 1:
    print(f"Очередь: {first_player}")
else:
    print(f"Очередь: {second_player}")

def input_value(player):
    x = int(input(f"{player}, сколько конфет возжелаешь в этот раз ты (от 1 до 28) ??? - "))
    while x < 1 or x > 28:
        x = int(input(f"{player}, Не считается ! Меньше одного брать нельзя ! - "))
    return x

def result(player, k, count, sweets):
    print(f"{player}, взял {k}, теперь у него {count}. На столе осталось {sweets} конфет.")

while sweets_table > 0:
    if turn == 1:
        k = input_value(first_player)
        first_count += k
        sweets_table -= k
        turn = 2
        result(first_player, k, first_count, sweets_table)
        continue
    else:
        k = input_value(second_player)
        second_count += k
        sweets_table -= k
        turn = 1
        result(second_player, k, second_count, sweets_table)
        continue

if turn == 2:
    print(f"Первый сладкоежка - {first_player} - победитель !!! {second_player} - остался голодным !!!")
else:
    print(f"Второй сладкоежка - {second_player} - победитель !!! {first_player} - остался голодным !!!")