# 21. 创建一个Rational类，执行带分数的算术运算。
# 用2个整数属性分别表示有理数的分子（numerator）和分母（denominator）。
# 默认分子值为0，分母为1。
# 提供6个方法（所有最后计算结果应为最简化形式）：
# （1）相加；（2）相乘；（3）相减；（4）相除；
# （5）以a/b的形式显示有理数，其中a为分子，b为分母。
# （6）以浮点数的形式显示有理数。

class Rational:
    def __init__(self, numerator=0, denominator=1):
        self.numerator = numerator
        self.denominator = denominator

    def __add__(self, other):
        return Rational(self.numerator * other.denominator + other.numerator * self.denominator,
                        self.denominator * other.denominator)

    def __sub__(self, other):
        return Rational(self.numerator * other.denominator - other.numerator * self.denominator,
                        self.denominator * other.denominator)

    def __mul__(self, other):
        return Rational(self.numerator * other.numerator, self.denominator * other.denominator)

    def __truediv__(self, other):
        return Rational(self.numerator * other.denominator, self.denominator * other.numerator)

    def __str__(self):
        return f"{self.numerator}/{self.denominator}"

    def __float__(self):
        return self.numerator / self.denominator

r1 = Rational(1, 2)
r2 = Rational(1, 3)
print(r1 + r2)
print(r1 - r2)
print(r1 * r2)
print(r1 / r2)
