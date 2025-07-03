# P021-水仙花数
# “水仙花数”是指一个三位正整数，其各位数字的立方和刚好等于该数本身，如：153＝1^3＋5^3＋3^3 
#（其中^表示乘方，5^3表示5的3次方），则153是一个“水仙花数”。
# 输入n, m，100<=n,m<1000, 求出[n,m]之间的水仙花数。若该区间没有水仙花数，输出-1.
# 输入：n,m，用空格隔开。
# 输出：若干水仙花数，用空格隔开（最后一位输出后面无空格）。


num = [int(x) for x in input().split()]
daffodil = []
for i in range(num[0], num[1]+1):
    digit = [int(x)**3 for x in str(i)]
    if i==sum(digit):
        daffodil.append(i)
if len(daffodil)==0:
    print("-1")
else:
    print(*daffodil)