# 2- Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
# Нужно написать таблицу истинности.
# Расшифровка символов логики:
# Значек предлога = Отрицание («не»)
# ∧ = Конъюнкция («и»)
# ∨ = Дизъюнкция («или»)
# Расшифровка выражения v1: НЕ(X ИЛИ Y ИЛИ Z) = НЕ X И НЕ Y И НЕ Z
# Расшифровка выражения v2: not (x or y or z) == (not x and not y and not z)

for x in range(2):
     for y in range(2):
         for z in range(2):
             print((x, y, z), '-',  (not (x or y or z) == (not x and not y and not z)))