import time


def inp():
    try:
        d, h, mi, s = map(int, input("Введите время в формате д ч м с: ").split())
        transform(d, h, mi, s)
    except ValueError:
        inv_form()


def transform(day, hou, m, sec):
    while sec > 59:
        m = m + sec // 60
        sec = sec % 60
    while m > 59:
        hou = hou + m // 60
        m = m % 60
    while hou > 23:
        day = day + hou // 24
        hou = hou % 24
    return main(day, hou, m, sec)


def main(day, hou, m, sec):
    for x in range(0, day+1):
        for y in range(0, hou+1):
            for z in range(0, m+1):
                for w in range(0, sec+1):
                    print(day, " ", hou, " ", m, " ", sec)
                    sec = sec - 1
                    time.sleep(1)
                sec = 59
                m = m - 1
            m = 59
            hou = hou - 1
        hou = 23
        day = day - 1
    print("Время закончилось.", end=" ")
    end()


def end():
    a = str(input("Ещё раз? (y/n): "))
    if a == 'y':
        inp()
    elif a == 'n':
        print("До свидания, хорошего дня!")
    else:
        print("Ошибка формы.", end=" ")
        end()


def inv_form():
    print("Неверная форма. Пожалуйста, введите снова: ")
    inp()