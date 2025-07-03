# P047-求给定区间中的孪生数的数量
# 所谓孪生素数是指间隔为 2 的相邻素数，例如最小的孪生素数是3和5,5和7也是孪生数。
# 编写程序，求给定区间[m,n]中的孪生数的数量。例如[2,10]中的孪生数有(3,5)和(5,7)，则[2,10]中孪生数的数量为2.
# 输入：正整数m,n,    m,n>1.
# 输出：[m,n]中的孪生的数量


def is_prime(x):
    for i in range(2, int(x**0.5)+1):
        if x%i == 0:
            return False
    return True

input = [int(x) for x in input().split()]
count = 0
for i in range(input[0], input[1]-1):
    if is_prime(i) and is_prime(i+2):
        count += 1
print(count)
