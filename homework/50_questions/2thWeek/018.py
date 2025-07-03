# P018-求a+aa+aaa+aaaa+…+aa...a
# 求a+aa+aaa+aaaa+…+aa...a（n个），其中a为1～9之间的整数。
# 例如：当a = 1, n = 3时，求1+11+111之和为123；
# 输入：组成序列的数字a和求和项的数量n
# 输出：算式和结果。


num = [int(x) for x in input().split()]
series = [num[0]]
for i in range(1, num[1]):
    series.append(series[i-1]*10+num[0])
print('+'.join(str(s) for s in series)+"="+str(sum(series)))