import math

from Functions.Function import AbstractFunction


class FirstFunction(AbstractFunction):
    const: float

    def __init__(self) -> None:
        super().__init__()

    def calc(self, x: float) -> float:
        return -math.exp(x) / (x * math.exp(x) + self.const)

    def calcDerivative(self, x: float, y: float) -> float:
        return y + (1 + x) * y ** 2

    def calcConst(self, x0, y0):
        Ex = math.exp(x0)  # e^x
        self.const = -Ex / y0 - x0 * Ex

    def __str__(self):
        return "y' = y + (1 + x) * y^2"
