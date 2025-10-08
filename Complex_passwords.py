from random import choices, shuffle, randint
from string import ascii_uppercase, ascii_lowercase

def distribution(settings, length):
    """
    Неравномерно распределяет количество символов в каждом виде настроек.

    Args:
        settings (list): список булевых значений настроек пароля
        length (int): длина пароля

    Returns:
        

    Raises:


    Example:
        >
    """
    number_of_conditions = sum(settings)
    n = number_of_conditions
    res = [0]*number_of_conditions
    for i in range(number_of_conditions):
        dif = length - sum(res) - n
        res[i] = randint(1, dif)
        n -= 1
    dif = length - sum(res)
    if dif == 0: return res
    res[randint(0, number_of_conditions-1)] += dif
    return res


def generate_password(settings="", length=0):
    """


    Args:


    Returns:


    Raises:


    Example:
        >
    """
    special = "!#$%&()*+,-./:;<=>?@[]^_`{|}~"
    nums = "0123456789"
    bool_settings = [0, 0, 0, 0]
    for i in settings:
        match i:
            case "1": bool_settings[0] = 1
            case "2": bool_settings[1] = 1
            case "3": bool_settings[2] = 1
            case "4": bool_settings[3] = 1
    quantity_distribution = distribution(bool_settings, length)
    password = (choices(ascii_lowercase, k = quantity_distribution[0]) +
                choices(ascii_uppercase, k = quantity_distribution[1]) +
                choices(special, k = quantity_distribution[2]) +
                choices(nums, k = quantity_distribution[3]))
    shuffle(password)
    return password

print("""Настройки пароля:
1. Наличие нижнего регистра
2. Наличие верхнего регистра
3. Наличие спец. символов
4. Наличие цифр""")
user_settings = input("Выберите настройки пароля (в любом порядке без пробелов): ")
user_password_length = int(input("Введите длину пароля: "))

print("\nРезультат:", "".join(generate_password(user_settings, user_password_length)), sep="\n")
input("\nНажмите Enter для выхода.")