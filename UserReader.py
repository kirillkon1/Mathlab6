from Functions.FirstFunction import FirstFunction
from Functions.Function import AbstractFunction
from Methods.AdamsMethod import AdamsMethod
from Methods.ImprovedEulerMethod import ImprovedEulerMethod


def userRead():
    fun = getFunc()
    a, b = getBorders()
    step = getH(fun.a, fun.b)
    eps = getEps()
    y = getY(a)

    meth = getMethod()

    return fun, meth, a, b, step, eps, y


def getH(a, b):
    print(f"Введи шаг (0 < h < {b - a})")
    while True:
        try:
            h = float(input())
            if b - a > h > 0:
                break
            print("Неверный ввод")
        except Exception:
            print("Неверный ввод")
    return h


def getY(a):
    print(f"Введите Y в точке {a}")
    while True:
        try:
            y = float(input())
            break
        except Exception:
            print("Неверный ввод")
    return y


def getEps():
    print("Введи точность вычисления: eps (0; 1)")
    while True:
        try:
            eps = float(input())
            if 1 > eps > 0:
                break
            print("Неверный ввод")
        except Exception:
            print("Неверный ввод")
    return eps


def getBorders():
    print("Введи два числа, которые будут границами дифференцирования (a, b)")
    while True:
        try:
            border = input().split()
            a, b = int(border[0]), int(border[1])

            if a < b:
                break
            else:
                tmp = a
                a = b
                b = tmp
                break

        except Exception:
            print("Неверный ввод")
    return a, b


def getFunc() -> AbstractFunction:
    print("Выберите функцию:\n"
          "1) y' = y + (1 + x) * y^2")

    num_func = int(input())

    return FirstFunction()


def getMethod():
    print("Выберите метод:\n"
          "1) Усовершенствованный метод Эйлера\n"
          "2) Метод Адамса")

    while True:
        try:
            num = int(input())
            if num == 1 or num == 2:
                break
            print("Неверный ввод")
        except Exception:
            print("Неверный ввод")

    return ImprovedEulerMethod() if num == 1 else AdamsMethod()
