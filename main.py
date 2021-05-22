import sys

from Util import drawGraphic, findFault, findRungeFault, toFixedFloat
from Functions.FirstFunction import FirstFunction
from Methods.AdamsMethod import AdamsMethod
from Methods.AdvancedEulerMethod import AdvancedEulerMethod
from UserReader import userRead
import numpy as np

x_list = []
y_list_adams = []
y_list_euler = []
y_list_correct = []  # Список точных решений

if __name__ == '__main__':


    function, a, b, step, y0 = userRead()  # fun, a, b, step
    fix = int(-np.log10(step) + 1)

    eulerMethod = AdvancedEulerMethod()
    adamsMethod = AdamsMethod()

    # Заполняю x с шагом step
    [x_list.append(np.around(i, fix)) for i in np.arange(a, b + 0.01, step)]

    y_list_correct.append(y0)
    function.calcConst(x_list[0], y_list_correct[0])  # Высчитываю const функции

    y_list_correct.clear()
    [y_list_correct.append(toFixedFloat(function.calc(i))) for i in x_list]

    try:
        y_tmp = [y_list_correct[0]]
        y_list_euler = eulerMethod.calculate(x_list, y_tmp, function)
    except OverflowError:
        print("ОШИБКА: ПЕРЕПОЛНЕНИЕ")
        sys.exit(-1)

    # Передаю массив решений 'y' для корректной работы метода
    try:
        y_list_adams = adamsMethod.calculate(x_list, y_list_euler, function)
    except OverflowError:
        print("ОШИБКА: ПЕРЕПОЛНЕНИЕ")
        sys.exit(-1)



    # # print(*[f"|| {'i':>1} || {'xi':>10} || {'yi Эйлер':> 10} || {'yi Адамс':> 10} || {'yi точн':>10 }"])
    #
    # for i in range(len(x_list)): print(*[ f"|| {i:>3} | {x_list[i]:>4} | {toFixedFloat(y_list_euler[i], 4):>10} | {
    # toFixedFloat(y_list_adams[i], 4):>10} | {toFixedFloat(y_list_correct[i], 4):>10}"])


    drawGraphic(x_list, y_list_euler, y_list_correct, title="График, составленный с помощью усовер. метода Эйлера", legend = eulerMethod)
    drawGraphic(x_list, y_list_adams, y_list_correct, title="График, составленный с помощью метода Адамса", legend = adamsMethod)

    # print(f"Погрешность: {findFault(x_list, y_list, y_list_correct)}")
    print(f"Погрешность метода Эйлера: {findRungeFault(x_list, y_list_euler, eulerMethod, function)}")
    print(f"Погрешность метода Адамса: {findRungeFault(x_list, y_list_euler, adamsMethod, function)}")
