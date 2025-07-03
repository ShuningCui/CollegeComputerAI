# 20. 创建一个SavingAccount类，一个类属性annualInterestRate保存全部账户所有人的年利率。
# 类的每个对象包含属性savingBalance，表示该账户当前的存款余额。
# 提供一个计算月利息的函数CalculateMonthlyInterest，
# 将savingBalance和annaulInterestRate相乘并除以12，
# 然后将该利息加到savingBalance中。提供一个函数ModifyInterestRate，
# 将annualInterestRate设置成一个新值。
# 编写程序，测试该类。

class SavingAccount:
    annualInterestRate = 0

    def __init__(self, savingBalance):
        self.savingBalance = savingBalance

    def calculateMonthlyInterest(self):
        self.savingBalance += self.savingBalance * SavingAccount.annualInterestRate / 12

    @classmethod
    def modifyInterestRate(cls, rate):
        cls.annualInterestRate = rate

savingAccount = SavingAccount(1000)
SavingAccount.modifyInterestRate(0.1)
savingAccount.calculateMonthlyInterest()
print(savingAccount.savingBalance)