import math

from Functions.Function import AbstractFunction


# При вводе y0 = 0 в функцию, программа ломается, т.к.
# при вычислении константы (производной постоянной) программа делит на ноль

# При вводе y0 > 0 программа ломается, т.к.
# вычисления слишком быстро возрастают => Overflow
class FirstFunction(AbstractFunction):
    const: float

    def __init__(self) -> None:
        super().__init__()

    # Высчитывание решенного дифф. уравнения.
    def calc(self, x: float) -> float:
        return -math.exp(x) / (x * math.exp(x) + self.const)

    # Высчитывание правой части дифф. уравнение (см. картинку Function1.png)
    def calcDerivative(self, x: float, y: float) -> float:
        return y + (1 + x) * y ** 2

    # Высчитывание константы (производной постоянной)
    def calcConst(self, x0, y0):
        Ex = math.exp(x0)  # e^x
        self.const = -Ex / y0 - x0 * Ex

    def __str__(self):
        return "y' = y + (1 + x) * y^2"
