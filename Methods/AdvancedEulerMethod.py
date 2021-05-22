from Functions.Function import AbstractFunction
from Methods.AbstractMethod import AbstractMethod
import numpy as np
import sys


class AdvancedEulerMethod(AbstractMethod):
    x_table = []
    y_table = []

    coefficient_accuracy = 4


    def calculate(self, x_list: list, y_list: list, func: AbstractFunction):
        self.x_table = x_list
        self.y_table = y_list

        h = self.x_table[1] - self.x_table[0]

        for i in range(len(self.y_table), len(self.x_table)):
            self.y_table.append(self.y_table[i - 1] + h / 2 * (
                    func.calcDerivative(self.x_table[i - 1], self.y_table[i - 1]) +
                    func.calcDerivative(self.x_table[i],
                                        self.y_table[i - 1] + h * func.calcDerivative(self.x_table[i - 1],
                                                                                      self.y_table[i - 1]))
            )
                                )
            # if self.y_table[i] >= np.inf:
            #     print(f"Error: AdvancedEulerMethod -> inf")
            #     sys.exit(-1)

        return self.y_table

    def __str__(self):
        return "Усов. метод Эйлера"