import time


day, hou, m, sec = map(int, input("время в формате д ч м с ").split())


def main():
    global day, hou, m, sec
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
    print("end")


main()
