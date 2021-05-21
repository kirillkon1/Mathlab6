from abc import ABC, abstractmethod


class AbstractFunction(ABC):
    const: float  # Константа от диф. уравнения
    a: float  # левая граница
    b: float  # правая граница
    step: float  # шаг разбиения
    eps: float  # точность

    def __init__(self) -> None:
        super().__init__()

    @abstractmethod
    def calc(self, x: float) -> float:
        pass

    @abstractmethod
    def calcDerivative(self, x: float, y: float) -> float:
        pass

    @abstractmethod
    def calcConst(self, x_list: list, y_list):
        pass

    def __str__(self):
        return "abc"
