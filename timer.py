import time


def timer(s):
    b = check(s)
    print(b)
    if s is None:
        start()
    elif s != 0:
        for i in range(0, s):
            print(s-i)
            time.sleep(1)
        print("0")
        tu()
    elif s == 0:
        tu()


def tu():
    inp = input("time's up! again? y/n: ")
    if inp == "y":
        try:
            s = int(input("type:tu "))
            timer(s)
        except ValueError:
            inv_form()
    elif inp == "n":
        print("bye!")
        exit()
    else:
        print("input error")
        tu()


def inv_form():
    print("invalid format. type again (0-59): ")
    try:
        s = int(input())
        return check(s)
    except ValueError:
        inv_form()


def check(s):
    if s >= 60 or s < 0:
        inv_form()
    elif s == 0:
        tu()
    else:
        print(s, "ss")
        return s


def start():
    s = int(input("type:s "))
    return timer(s)


start()


#
# import time
#
#
# def start():
#     s = int(input("secs: "))
#     if s > 59 or s < 0:
#         print("invalid format, type 0-59: ")
#         start()
#     elif s == 0:
#         print("zero")
#         start()
#     else:
#         for i in range(0, s):
#             print(s-i)
#             time.sleep(1)
#         print("0")
#     return start()
#
#
# start()