# 18. 设计并测试一个名为Ellipse的椭圆类，其属性为外接矩形的左上角与右下角两个点的坐标，
# 并能计算出椭圆的面积。

import math

class Ellipse:
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
    
    def area(self):
        a = abs(self.x1 - self.x2) / 2
        b = abs(self.y1 - self.y2) / 2
        return math.pi * a * b

ellipse = Ellipse(0, 0, 2, 1)
print(ellipse.area())