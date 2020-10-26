from random import randint, uniform


def rufje():
    before_sitting = randint(15, 21)
    after_sitting = randint(25, 30)
    after_2min = randint(15 + 5, 21 + 5)

    print("Ваш ЧСС спокою до присідань: " + str(before_sitting))
    print("Ваш ЧСС спокою після присідань: " + str(after_sitting))
    print("Ваш ЧСС спокою після 2хв відпочинку: " + str(after_2min))

    css = ((after_sitting + before_sitting+after_2min) * 4-200) / 10
    print("Руф'є: " + str(css))


# рухові тести та нормативи
def page4():
    print('Згинання розгинання рук в упорі лежачи: ', randint(20, 40))
    print("Човниковий біг 4x9: " + str(uniform(9, 9.4)))
    print("Нахили тулуба вперед: " + str(randint(15, 18)))
    print("Біг 100м з високого старту: " + str(uniform(22.2, 23.3)))

def page6():
    days = int(input("Введіть кількість днів в місяці: "))
    summa = 0
    for x in range(1, days + 1):
        number = randint(60, 76)
        summa += number
        print('Ваш ранковий пульс дня ' + str(x) + " " + str(number))
    print('Середнє значення: ' + str(summa / days))


def valdfogel():
    before = randint(60, 84)
    after = randint(70, 94)
    print('Before: ', before)
    print('After: ', after)
    print('Vogel: ', (after-before))
