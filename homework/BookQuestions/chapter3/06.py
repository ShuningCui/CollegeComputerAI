# 6. 编写计算阶乘 n!的程序。

def factorial(n):
    if n == 0:
        return 1
    else:
        for i in range(1, n):
            n *= i
        return n

n = int(input("请输入一个整数："))
print(f"{n}! = {factorial(n)}")