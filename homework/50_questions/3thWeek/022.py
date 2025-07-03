# P022-求勾股数
# 若三个正整数a,b,c满足 a^2+b^2=c^2，则它们是一组勾股数。(^2表示平方，a^表示a的平方)。
# 编写程序，求给定区间[m,n]中的勾股数的数量(设一组勾股数满足a<b<c)。
# 例如[1,10]中的勾股数有(3,4,5)和(6,8,10)，则[1,10]中勾股数的数量为2。
# 输入：正整数m,n,   空格分隔
# 输出：[m,n]中的勾股数的数量


num = [int(x) for x in input().split()]
count = 0
for i in range(num[0], num[1]+1):
    for j in range(i, num[1]+1):
        for k in range(j, num[1]+1):
            if i*i+j*j==k*k:
                count += 1
print(count)
