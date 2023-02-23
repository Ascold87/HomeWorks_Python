# 4- Шифр Цезаря - это способ шифрования, где каждая буква смещается на определенное количество символов влево или вправо. 
# При расшифровке происходит обратная операция.
# К примеру, слово "абба" можно зашифровать "бввб" - сдвиг на 1 вправо. 
# "вггв" - сдвиг на 2 вправо, "юяяю" - сдвиг на 2 влево.
# Сдвиг часто называют ключом шифрования.
# Ваша задача - написать функцию, которая записывает в файл шифрованный текст, 
# а также функцию, которая спрашивает ключ, считывает текст и дешифровывает его.

def cipher_cesarius_input(n_shift = int(input("Введите ключ шифрования (до 35ти): "))
                        ,str1 = (input("Введите текст: "))) -> str:
        alphabet = list('абвгдеёжзийклмнопрстуфхцчшщъыьэюя,.: абвгдеёжзийклмнопрстуфхцчшщъыьэюя,.: ')
        str1 = str1.lower()
        cifr_text = ''
        for i in str1:
            mesto = alphabet.index(i)
            new_mesto = mesto + n_shift
            if i in alphabet:
                cifr_text += alphabet[new_mesto]
            else:
                print("Введено недопустимое значение.")
                break
        with open ('file_code.txt', 'w') as file:
            file.write(cifr_text)
        return cifr_text


print(f'Ваш зашифрованный текст: {cipher_cesarius_input()}')
tex = cipher_cesarius_input()

def transcrypt_cipher_cesarius(key = int(input("Введите ключ для дешифровки: "))) ->str:
    with open('file_code.txt', 'r') as file:
        chif_text = file.read()
    alphabet = list('абвгдеёжзийклмнопрстуфхцчшщъыьэюя,. : абвгдеёжзийклмнопрстуфхцчшщъыьэюя,.: ')[::-1]
    dechif_text = ''
    for i in chif_text:
        mesto = alphabet.index(i)
        new_mesto = mesto + key
        if i in alphabet:
            dechif_text += alphabet[new_mesto]
    with open('file_encode.txt', 'a') as file:
        file.write(f'{dechif_text} \n')
    return dechif_text

print(f'Расшифровка: {transcrypt_cipher_cesarius()}')