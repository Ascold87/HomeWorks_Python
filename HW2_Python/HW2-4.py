# 4 - По кругу стоят [n] человек.
# Ведущий посчитал [m] человек по кругу, начиная с первого.
# При этом каждый из тех, кто участвовал в этом счете, получил по одной монете, остальные получили по две монеты.
# Далее человек, на котором остановился счет, отдает все свои монеты следующему по счету человеку, а сам выбывает из круга.
# Процесс продолжается с места остановки аналогичным образом до последнего человека в круге.
# Составьте алгоритм, который проводит эту игру. Если хотите делать паузы,
# то импортируйте библиотеку time и используйте оттуда функцию sleep.
# Определите номер этого человека и количество монет, которые оказались у него в конце игры.

whole_num = 5
choose_num = 3
num_two_coin = whole_num - choose_num
num = choose_num - 1
list_partic = [1] * whole_num
for choose_num in list_partic:
    list_partic[choose_num] += 2
while whole_num > 0:
    list_partic[:] = [1] * choose_num
    second_group = [2] * num_two_coin
    list_partic = first_group + second_group
    list_partic.insert(choose_num, list_partic[num] + list_partic[choose_num])
    list_partic.pop(num)
    list_partic.pop(-1)
    whole_num -= 1
while whole_num > 0:
    poor_list = [x+1 for x in first_group]
    whole_num -= 1

def game_with_coins(whole_num, choose_num):
    whole_num = 5
    choose_num = 2
    num_two_coin = whole_num - choose_num
    list_partic = [1] * choose_num + [2] * num_two_coin
print(list_partic)
new_partic = []
k = 0
p = 0
x = 0

while k <= whole_num:
    new_partic.append(list_partic[k])
    k += 1

new_partic[choose_num] = list_partic[choose_num - 1] + list_partic[choose_num]
new_partic.pop(choose_num - 1)
whole_num = whole_num - 1

print(new_partic)

whole_num = whole_num - 1


print(new_partic)

x = 0
x = list_partic[i]+list_partic[i+1]
new_partic.append(x)
print(new_partic)
while i > 0:
    new_partic.append(list_partic[i])
    i -= 1

new_partic.append(list_partic[i])
x = list_partic[i]+list_partic[i+1]
new_partic.append(x)

list_partic.insert(choose_num, list_partic[num]+list_partic[choose_num])
list_partic.pop(num)
