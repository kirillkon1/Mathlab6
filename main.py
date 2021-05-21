import sys

from Util import drawGraphic, findFault, findRungeFault
from Functions.FirstFunction import FirstFunction
from Methods.AdamsMethod import AdamsMethod
from Methods.ImprovedEulerMethod import ImprovedEulerMethod
from UserReader import userRead
import numpy as np

step = 0.1
fix = int(-np.log10(step) + 1)
eps = 0.001
border = [1, 1.5]
y0 = -1
a, b = border[0], border[1]
x_list, y_list = [], []
function = FirstFunction()
y_list_correct = []

if __name__ == '__main__':

    # function, method, a, b, step, eps, y0 = userRead()  # fun, meth, a, b, step, eps

    eulerMethod = ImprovedEulerMethod()
    adamsMethod = AdamsMethod()

    [x_list.append(np.around(i, fix)) for i in np.arange(a, b + 0.01, step)]

    y_list.append(y0)
    function.calcConst(x_list[0], y_list[0])

    for i in x_list:
        y_list_correct.append(function.calc(i))

    try:
        y_list = eulerMethod.calculate(x_list, y_list, function)
    except OverflowError:
        print("ОШИБКА: ПЕРЕПОЛНЕНИЕ")
        sys.exit(-1)

    print("По методу усов. Эйлера")
    print(*[f"|| {'i':>1} || {'xi':>{fix + 1}} || {'yi':>{fix}}"])

    y_list = adamsMethod.calculate(x_list, y_list, function)
    # for i in range(len(x_list)):
    #     print(*[f"|| {i:>1} || {x_list[i]:>{fix}} || {y_list_correct[i]:>{fix}}"])


    drawGraphic(x_list, y_list, y_list_correct, title="График, составленный с помощью метода")
    drawGraphic(x_list, y_list, y_list_correct, title="График с точными значениями")

    print(f"Погрешность: {findFault(x_list, y_list, y_list_correct)}")
    # print(f"Погрешность: {findRungeFault(x_list, y_list, adamsMethod, function)}")

