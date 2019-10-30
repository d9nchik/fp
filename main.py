from random import randint, uniform


def page5():
    before_sitting = randint(30, 38)
    after_sitting = randint(50, 60)
    after_2min = randint(30 + 5, 38 + 5)

    print("Ваш ЧСС спокою до присідань: " + str(before_sitting))
    print("Ваш ЧСС спокою після присідань: " + str(after_sitting))
    print("Ваш ЧСС спокою після 2хв відпочинку: " + str(after_2min))

    css = (after_sitting - before_sitting) * 100 / before_sitting
    print("ЧСС ПДН: " + str(css))

    f4s = before_sitting + after_2min
    print("ФССС: " + str(f4s))


# рухові тести та нормативи
def page4():
    print("Човниковий біг 4x9: " + str(uniform(9, 9.4)))
    print("Нахили тулуба вперед: " + str(randint(15, 18)))
    print("Біг 100м з високого старту: " + str(uniform(22.2, 23.3)))


# Сторінка 6
def page6():
    days = int(input("Введіть кількість днів в місяці: "))
    summa = 0
    for x in range(1, days + 1):
        number = randint(60, 76)
        summa += number
        print('Ваш ранковий пульс дня ' + str(x) + " " + str(number))
    print('Середнє значення: ' + str(summa / days))
