# 17. 定义一个Dog类，包含name、age、gender、weight
# 等属性以及对这些属性操作的方法。
# 实现并测试这个类。

class Dog:
    def __init__(self) -> None:
        self.name = ""
        self.age = 0
        self.gender = ""
        self.weight = 0
    
    def set_name(self, name):
        self.name = name
    
    def set_age(self, age):
        self.age = age
    
    def set_gender(self, gender):
        self.gender = gender
    
    def set_weight(self, weight):
        self.weight = weight

dog1 = Dog()
dog1.set_name("dog1")
dog1.set_age(1)
dog1.set_gender("male")
dog1.set_weight(10)