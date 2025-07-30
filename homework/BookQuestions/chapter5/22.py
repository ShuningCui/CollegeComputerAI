# 22. 邮局或快递公司投递包裹，提供不同的投递类型。
# 如3日内送达或次晨达，不同的类型费用不同。
# 创建一个继承层次来表示不同类型的包裹。
# 将Package类作为父类，将ThreeDayPackage类和OvernightPackage类作为它的派生类。
# 父类Package包含发件人和收件人的姓名，地址，城市，省，邮政编码及包裹的重量，单位克。
# 以及包裹投递标准费用，单位是克/元。
# Package类包含必要的构造函数来初始化这些变量，并保证变量的值具有一定的合理性，如重量需要大于0等。
# Packeage类包含一个函数CalculateCost计算包裹的基本费用公式是重量*投递标准费用。
# ThreeDayPackage继承自Package，含有一个固定费率的成员变量。
# 最终的投递费用为固定费率+标准费率（标准费率通过Package类的CalculateCost方法计算出。
# OvernightPackage和ThreeDayPackage相似，只是固定费率较高。
# 编写测试程序，创建不同类型的包裹计算投递费用。

class Package:
    def __init__(self, sender_name, sender_address, sender_city, sender_province, sender_postcode,
                 receiver_name, receiver_address, receiver_city, receiver_province, receiver_postcode,
                 weight, standard_rate):
        self.sender_name = sender_name
        self.sender_address = sender_address
        self.sender_city = sender_city
        self.sender_province = sender_province
        self.sender_postcode = sender_postcode
        self.receiver_name = receiver_name
        self.receiver_address = receiver_address
        self.receiver_city = receiver_city
        self.receiver_province = receiver_province
        self.receiver_postcode = receiver_postcode
        self.weight = weight if weight > 0 else 0
        self.standard_rate = standard_rate

    def calculate_cost(self):
        return self.weight * self.standard_rate

class ThreeDayPackage(Package):
    def __init__(self, sender_name, sender_address, sender_city, sender_province, sender_postcode,
                 receiver_name, receiver_address, receiver_city, receiver_province, receiver_postcode,
                 weight, standard_rate, fixed_rate):
        super().__init__(sender_name, sender_address, sender_city, sender_province, sender_postcode,
                         receiver_name, receiver_address, receiver_city, receiver_province, receiver_postcode,
                         weight, standard_rate)
        self.fixed_rate = fixed_rate

    def calculate_cost(self):
        return self.fixed_rate + super().calculate_cost()

class OvernightPackage(Package):
    def __init__(self, sender_name, sender_address, sender_city, sender_province, sender_postcode,
                 receiver_name, receiver_address, receiver_city, receiver_province, receiver_postcode,
                 weight, standard_rate, fixed_rate):
        super().__init__(sender_name, sender_address, sender_city, sender_province, sender_postcode,
                         receiver_name, receiver_address, receiver_city, receiver_province, receiver_postcode,
                         weight, standard_rate)
        self.fixed_rate = fixed_rate

    def calculate_cost(self):
        return self.fixed_rate + super().calculate_cost()

package = Package("sender", "address", "city", "province", "postcode",
                    "receiver", "address", "city", "province", "postcode",
                    100, 1)
print(package.calculate_cost())

three_day_package = ThreeDayPackage("sender", "address", "city", "province", "postcode",
                    "receiver", "address", "city", "province", "postcode",
                    100, 1, 10)
print(three_day_package.calculate_cost())

overnight_package = OvernightPackage("sender", "address", "city", "province", "postcode",
                    "receiver", "address", "city", "province", "postcode",
                    100, 1, 20)
print(overnight_package.calculate_cost())

