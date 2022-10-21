class Function:
    def __init__(self, param1, param2, operator):
        self.param1 = param1
        self.param2 = param2
        self.operator = operator

    def summa(self):
        return self.param1 + self.param2

    def definition(self):
        return self.param1 - self.param2

    def mul(self):
        return self.param1 * self.param2

    def div(self):
        if self.param2 == 0:
            return "На 0 делить нельзя"
        else:
            return round(self.param1 / self.param2, 2)

    def result(self):
        if self.operator == "+":
            return self.summa()
        elif self.operator == "-":
            return self.definition()
        elif self.operator == "*":
            return self.mul()
        elif self.operator == "/":
            return self.div()
        else:
            return str(self.param1) + self.operator + str(self.param2)

    def method(self):
        pass

    def __add__(self, other):
        return "разница первых параметров: " + str(self.param1 - other.param1) + "\n разница вторых параметров: " + str(
            self.param2 - other.param2)


class SumOfThree(Function):
    def method(self, param3):
        return self.summa() + param3


class DefWithDiv(Function):
    def method(self):
        if self.param2 != 0:
            return self.definition() / float(self.param2)
        else:
            return str(self.definition()) + "/0"


class Pow(Function):
    def mul(self):
        res = 1
        for i in range(int(self.param2)):
            res *= self.param1
        return res

    def method(self):
        return self.mul()


a = float(input("Введите первый параметр: "))
b = float(input("Введите второй параметр: "))
op = input("Введите операцию: ")
func = Function(a, b, op)
func2 = Function(5, 10, '-')
print(func.result())
print(func + func2)

sum_of_three = SumOfThree(a, b, op)
print(sum_of_three.method(3))
def_with_div = DefWithDiv(a, b, op)
print(def_with_div.method())
power = Pow(a, b, op)
print(power.method())
