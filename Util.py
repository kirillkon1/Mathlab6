import matplotlib.pyplot as plt
import numpy as np

# метод для отрисовки графика(-ов)
from Functions.Function import AbstractFunction
from Methods.AbstractMethod import AbstractMethod
from Methods.AdvancedEulerMethod import AdvancedEulerMethod


def drawGraphic(x_coords: list, y_coords: list, y_coords_correct: list, title=None, legend=None) -> None:
    ax = plt.gca()
    # ax.spines['left'].set_position('zero')
    # ax.spines['bottom'].set_position('zero')
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    plt.plot(x_coords, y_coords, 'r')
    plt.plot(x_coords, y_coords_correct, 'b')
    plt.legend([legend, "Точное решение"])
    plt.title(title)
    # plt.scatter(x_coords, y_coords)

    plt.show()


def findFault(x_list: list, y_list: list, y_list_correct: list):
    eps = 0

    for i in range(len(x_list)):
        eps_tmp = abs(y_list[i] - y_list_correct[i])
        if eps_tmp > eps:
            eps = eps_tmp

    return eps


# Погрешность по Рунге
def findRungeFault(x_list: list, y_list: list, method: AbstractMethod, func: AbstractFunction):
    y_list_half_step = []
    x_list_half_step = []
    methodEuler = AdvancedEulerMethod()
    step = x_list[1] - x_list[0]
    step = step / 2

    for i in np.arange(x_list[0], x_list[len(x_list) - 1] + 0.0001, step):
        x_list_half_step.append(float(np.around(i, int(-np.log10(step)) + 1)))

    y_list_half_step.append(y_list[0])
    y_list_half_step = methodEuler.calculate(x_list_half_step, y_list_half_step, func)
    y_list_half_step = method.calculate(x_list_half_step, y_list_half_step, func)

    faultR = 0
    for i in np.arange(len(x_list) - 1):
        tmp_R = (y_list[i] - y_list_half_step[i * 2]) / (2 ** method.coefficient_accuracy - 1)

        if tmp_R > faultR:
            faultR = tmp_R
        pass
    return faultR

def toFixedFloat(numObj, digits=2):
    return float(f"{numObj:.{digits}f}")
