def f(x, symbols):
    l = ("", "0", "00", "000", "01", "1", "10", "100", "1000", "02")
    return ''.join(symbols[int(i)] for i in l[x])

def convert_roman_to_arabic(roman_number):
    numbers = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    arabic_numbers = list(map(numbers.get, roman_number))
    for i in range(len(roman_number)-1):
        if arabic_numbers[i] < arabic_numbers[i+1]:
            arabic_numbers[i] = -arabic_numbers[i]
    return sum(arabic_numbers)

def convert_arabic_to_roman(arabic_number):
    arabic_number = int(arabic_number)
    thousands = arabic_number // 1000
    arabic_number %= 1000
    hundreds = arabic_number // 100
    arabic_number %= 100
    tens = arabic_number // 10
    arabic_number %= 10
    ones = arabic_number
    return f(thousands, "M") + f(hundreds, "CDM") + f(tens, "XLC") + f(ones, "IVX")

def converter(list_of_numbers):
    result = []
    for number in list_of_numbers:
        is_roman = number[0].isalpha()
        if is_roman:
            result.append(convert_roman_to_arabic(number))
        else:
            result.append(convert_arabic_to_roman(number))
    return result

list_of_numbers = input("Введите список римских или арабских цифр: \n").split()
roman_test = ["IV", "IX", "XLII", "XCIX", "MMXXIII"]

print("\nРезультат:", converter(list_of_numbers),sep="\n")
input("\nНажмите Enter для выхода.")