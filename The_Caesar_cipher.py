from string import ascii_uppercase, ascii_lowercase

def caesar_encode(string, key=0):
    result = ""
    ru_alphabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
    if any(1 for i in ru_alphabet if i in string):
        alphabet_lower = ru_alphabet[:33]
        alphabet_upper = ru_alphabet[33:]
    else:
        alphabet_lower = ascii_lowercase
        alphabet_upper = ascii_uppercase
    len_alphabet = len(alphabet_lower)
    for i in range(len(string)):
        if string[i] in "!#$%&'()*+,-./:;<=>?@[]^_`{|}~ ":
            result += string[i]
        elif string[i] == string[i].upper():
            result += alphabet_upper[(alphabet_upper.find(string[i]) + key) % len_alphabet]
        else:
            result += alphabet_lower[(alphabet_lower.find(string[i]) + key) % len_alphabet]
    return result

def caesar_decode(string, key=0):
    result = ""
    ru_alphabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
    if any(1 for i in ru_alphabet if i in string):
        alphabet_lower = ru_alphabet[:33]
        alphabet_upper = ru_alphabet[33:]
    else:
        alphabet_lower = ascii_lowercase
        alphabet_upper = ascii_uppercase
    len_alphabet = len(alphabet_lower)
    for i in range(len(string)):
        if string[i] in "!#$%&'()*+,-./:;<=>?@[]^_`{|}~ ":
            result += string[i]
        elif string[i] == string[i].upper():
            result += alphabet_upper[(alphabet_upper.find(string[i]) - key) % len_alphabet]
        else:
            result += alphabet_lower[(alphabet_lower.find(string[i]) - key) % len_alphabet]
    return result

print("1. Зашифровать сообщение\n"
      "2. Расшифровать сообщение")
n = input("Выберите действие: ")
user_string = input("Введите сообщение: ")
offset = int(input("Введите сдвиг: "))
if n == "1":
    print("Результат:")
    print(caesar_encode(user_string, offset))
elif n == "2":
    print("Результат:")
    print(caesar_decode(user_string, offset))

input("Нажмите Enter для выхода.")