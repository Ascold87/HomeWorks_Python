# 3 - В файле, содержащем фамилии студентов и их оценки, изменить на буквы в верхнем регистре тех студентов, которые имеют средний балл более «4».
# Нужно перезаписать файл.
# Пример:
# Ангела Меркель 5
# Энакин Скайуокер 5
# Фредди Меркури 3
# Александр Пушкин 4
# ================
# Программа выдаст:
# АНГЕЛА МЕРКЕЛЬ 5
# ЭНАКИН СКАЙУОКЕР 5
# Фредди Меркури 3
# Александр Пушкин 4

def write_to_file(str = 
'''Айболит 5
Терминатор 5
ОрбитБезСахара 2
ПетрПервый 3
Рафаэль 5'''):
    with open ('file1.txt','w') as file:
        file.write(str)
def rewrite_data():
    with open('file1.txt', 'r') as file1, open('file2.txt', 'w') as text2:
        lines = file1.readlines()
        char = '5'
        for line in lines:
            if char in line:
                new_data = line.replace(line, line.upper())
                text2.write(new_data)
            else:
                text2.write(line)
write_to_file()
rewrite_data()