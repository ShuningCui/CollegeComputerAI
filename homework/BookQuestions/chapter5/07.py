# 7. 编写程序求斐波那契数列的第n项和前n项之和。

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        a, b = 0, 1
        for i in range(2, n + 1):
            a, b = b, a + b
        return b

n = int(input("请输入一个整数："))
print(f"第{n}项：{fibonacci(n)}")