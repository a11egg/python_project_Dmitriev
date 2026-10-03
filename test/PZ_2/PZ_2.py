# Вариант 12
# Дано двузначное число. Найти сумму и произведение его цифр

def invalid_a(n: str) -> bool :
    return not (len(a) == 2)

while True:
    try:
        a = input("Введите двузначное число:")

        if invalid_a(a):
            print("Некорректный ввод! Попробуйте снова:")
            continue

        b = int(a[0])
        c = int(a[1])

        print("Сумма цифр: " + str(b+c))
        print("Произведение цифр: " + str(b*c))

    except :
        print("Ошибка! Введите целочисленное число:")
