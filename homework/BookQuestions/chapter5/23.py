# 23. 创建一个继承层次，银行用来表示客户的账户情况。
# 所有客户可以用其账户存款和取款。此外，还有更具体的账户类型。
# 例如，储蓄账户可以收取存款利息，而支票账户则需要为每一笔交易付给银行服务费。
# 创建父类Account和派生类SavingsAccount和CheckinAccount。
# 基类Account包括一个decimal类型的实例属性，表示账户结余。
# 这个类提供一个构造函数，接收初始结余并初始化实例变量。
# 构造函数要检验初始结余，确保其大于或等于0.0，否则将初始结余设置为0.0并显示一个错误消息，表示初始结余无效。
# 类提供两个方法。Credit方法将一定数量的资金存入账户，而Debit方法从账户中取款，确保取款的量不超过账户结余，
# 否则结余保持不变，并打印一个消息“Debit amount exeeded account balance”。
# 类要提供一个函数，返回当前结余。
# 派生类SavingsAccount继承Account的功能，
# 包括一个decimal实例属性，表示Account指定的利率（百分率）。
# SavingsAccount的构造函数接收初始结余和利率初值。
# SavingsAccount提供公用函数CalculateInterest，返回一个decimal值，
# 表示账户得到的利息。calculatelnterest方法将利率乘以账户结余求出利息值。
# SavingsAccount应该继承Credit与Debit方法而不需要重新定义。
# 派生类CheckingAccount继承Accout的功能，但包括一个decimal实例变量，
# 表示每笔交易的费用。CheckingAccount的构造函数接收初始结余和表示费用的参数。
# CheckingAccount类要重定义Credit与Debit函数，使事务执行成功时账户结余中减去手续费。
# CheckingAocount的Debit方法只在实际取钱时才扣除费用（即确保所取的量不超过账户结余）。
# 定义这个层次中的类之后，写一个程序，创建每个类的对象并测试其方法。
# 用Calculatelnterest方法将利息加进SavingsAccount对象，然后将返回的利息值传入对象的Credit方法

from decimal import Decimal

class Account:
    def __init__(self, balance: Decimal):
        if balance < 0:
            self.balance = Decimal(0)
            print("初始结余无效")
        else:
            self.balance = balance

    def credit(self, amount: Decimal):
        self.balance += amount

    def debit(self, amount: Decimal):
        if amount > self.balance:
            print("Debit amount exceeded account balance")
        else:
            self.balance -= amount

    def get_balance(self):
        return self.balance

class SavingsAccount(Account):
    def __init__(self, balance: Decimal, rate: Decimal):
        super().__init__(balance)
        self.rate = rate

    def calculate_interest(self):
        return self.balance * self.rate

class CheckingAccount(Account):
    def __init__(self, balance: Decimal, fee: Decimal):
        super().__init__(balance)
        self.fee = fee

    def credit(self, amount: Decimal):
        super().credit(amount - self.fee)

    def debit(self, amount: Decimal):
        if amount > self.balance:
            print("Debit amount exceeded account balance")
        else:
            super().debit(amount + self.fee)

savings_account = SavingsAccount(100, Decimal("0.1"))
savings_account.credit(savings_account.calculate_interest())
print(savings_account.get_balance())

