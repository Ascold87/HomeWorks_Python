# 2 - Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности. Не использовать множества.
# Постарайтесь решить за одно условие
# [1,1,1,1,2,2,2,3,3,3,4] -> [1,2,3,4]

print('Программа выведет список неповторяющихся элементов.')

def uniq_elts(elts: list) -> list:
    elts += [0]
    new_list = []
    index = 1
    new_list.append(elts[0])
    while index < len(elts)-1:
        if elts[index] in elts[index+1]:
            new_list.append(elts[index])
        index += 1
    return new_list, elts

print(f'Лист:{uniq_elts([])}')

# Решение неверное.
