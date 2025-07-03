# 19. 创建一个Rectangle类。这个类具有属性length和width，
# 以及包含成员周长（Perimeter）和面积（Area）。
# 成员函数Set设置并验证length和width都是大于0且小于20的浮点数。
# 编写该类计算周长和面积并验证。

class Rectangle:
    def __init__(self):
        self.length = 0
        self.width = 0

    def set(self, length, width):
        if 0 < length < 20 and 0 < width < 20:
            self.length = length
            self.width = width
        else:
            raise ValueError("length and width should be greater than 0 and less than 20")

    def perimeter(self):
        return 2 * (self.length + self.width)

    def area(self):
        return self.length * self.width

rectangle = Rectangle()
rectangle.set(10, 5)
print(rectangle.perimeter())
print(rectangle.area())