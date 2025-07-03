# P019-找出给定范围内是7的倍数或带7的全部正整数
# 编写程序，找出[m,n]范围内是7的倍数或带7的全部正整数(注意：如果一个是既是7的倍数又是带7的数，
# 就输出2次，先输出倍数，再输出带7的整数，如：7 is a multiple of 7 7 contains 7)。
# 其中，m和n为正整数。
# 样例
# 1 20
# 7 is a multiple of 7
# 7 contains 7
# 14 is a multiple of 7
# 17 contains 7


num = [int(x) for x in input().split()]
for i in range(num[0], num[1]+1):
    if i%7==0:
        print(f"{i} is a multiple of 7")
    if "7" in str(i):
        print(f"{i} contains 7")