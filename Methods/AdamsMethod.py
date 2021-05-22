from Functions.Function import AbstractFunction
from Methods.AbstractMethod import AbstractMethod
import numpy as np


class AdamsMethod(AbstractMethod):
    x_table: list
    y_table: list
    func: AbstractFunction

    coefficient_accuracy = 4

    def calculate(self, x_list: list, y_list: list, func: AbstractFunction):

        if len(y_list) < 4:
            print('Метод Адамса: для вычисление данным методом необходимо минимум 4 \'y\' ')
            return

        self.x_table = x_list
        self.y_table = y_list
        self.func = func

        h = self.x_table[1] - self.x_table[0]

        for i in range(3, len(self.x_table)):
            tmp = self.y_table[i - 1] + \
                  h * self.func.calcDerivative(self.x_table[i - 1], self.y_table[i - 1]) + \
                  h ** 2 * 1 / 2 * self.calcFirstFiniteDifferences(i - 1) + \
                  h ** 3 * 5 / 12 * self.calcSecondFiniteDifferences(i - 1) + \
                  h ** 4 * 3 / 8 * self.calcThirdFiniteDifferences(i - 1)

            tmp = float(toFixed(tmp, int(-np.log10(self.func.eps))))
            self.y_table[i] = tmp

        return self.y_table

    # {i} - индекс
    # DELTA f{i} = f{i} - f{i-1}
    def calcFirstFiniteDifferences(self, index):
        return self.func.calcDerivative(self.x_table[index], self.y_table[index]) \
               - self.func.calcDerivative(self.x_table[index - 1], self.y_table[index - 1])

    # DELTA^2 f{i} = f{i} - 2f{i-1} + f{i-2}
    def calcSecondFiniteDifferences(self, index):
        return self.func.calcDerivative(self.x_table[index], self.y_table[index]) \
               - 2 * self.func.calcDerivative(self.x_table[index - 1], self.y_table[index - 1]) + \
               self.func.calcDerivative(self.x_table[index - 2], self.y_table[index - 2])

    # DELTA^3 f{i} = f{i} - 3f{i-1} + 3f{i-2} - f{i-3}
    def calcThirdFiniteDifferences(self, index):
        return self.func.calcDerivative(self.x_table[index], self.y_table[index]) - \
               3 * self.func.calcDerivative(self.x_table[index - 1], self.y_table[index - 1]) + \
               3 * self.func.calcDerivative(self.x_table[index - 2], self.y_table[index - 2]) - \
               self.func.calcDerivative(self.x_table[index - 3], self.y_table[index - 3])

    def __str__(self):
        return "Метод Адамса"

def toFixed(numObj, digits=2):
    return f"{numObj:.{digits}f}"
