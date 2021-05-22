from abc import ABC, abstractmethod

from Functions.Function import AbstractFunction


class AbstractMethod(ABC):
    coefficient_accuracy: int = 1  # порядок точности метода

    @abstractmethod
    def calculate(self, x_list, y_list, func: AbstractFunction):
        pass
