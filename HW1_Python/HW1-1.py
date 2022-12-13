# 1- Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.
# Дополнительно: можете проверить, что это действительно число, и что это действительно входит в нужный диапазон.

print('Введите номер дня недели: ')
print('Enter the number of the day of the week:')
week_day = int(input())
if 0 < week_day < 8:
    if week_day < 6:
        print('Это будний день.')
        print("It's a weekday now. You should to go to work.")
    else:
        print("Это выходной. И помните, к понедельнику вам следует быть огурцом.")
        print("It's a weekend now. You should to go to some pub.")
else:
    print("Это вообще не день недели.")
    print("It isn't a day week.")
