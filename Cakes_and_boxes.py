def print_pack_report(order):
    for n in range(order, 0, -1):
        res = str(int(n%5 == 0)) + str(int(n%3 == 0))
        match res:
            case "11":
                yield f"{n} - расфасуем по 3 и по 5"
            case "10":
                yield f"{n} - расфасуем по 5"
            case "01":
                yield f"{n} - расфасуем по 3"
            case "00":
                yield f"{n} - не заказываем!"

for i in print_pack_report(int(input("Введите количество пирожных: "))): print(i)
input("\nНажмите Enter для выхода.")