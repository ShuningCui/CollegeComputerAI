# P005-最大公约数
# 求n个数的最大公约数。其中：2<=n<50
# 输入：n个正整数，用空格隔开，在一行内输入。
# 输出：最大公约数和这n个数，用一个空格隔开。

import math
num = [int(x) for x in input().split()]
print(math.gcd(*num))
print(*num)
