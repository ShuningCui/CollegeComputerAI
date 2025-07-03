# 11. 求a+aa+aaa+aaaa+... ...+aa...a（n个），其中a为1～9之间的整数。
#  		例如：当a = 1, n = 3时，求1+11+111之和；
# 当a = 5, n = 7时，求5＋55＋555＋5555＋55555＋5555555之和。

def sum_series(a, n):
    total = a
    for i in range(2, n + 1):
        total += int(str(a) * i)
    return total

a,n = [int(x) for x in input("请输入a和n：").split(' ')]
print(sum_series(a, n))
