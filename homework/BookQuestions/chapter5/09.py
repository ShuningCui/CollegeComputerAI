# 9. 从键盘输入一个正整数，然后将该整数分解为1和各个质因子的相乘，
# 如果输入的整数本身就是质数，则应分解为1和该数本身相乘。

def prime_factors(n):
    factors = [1]
    for i in range(2, n + 1):
        while n % i == 0:
            factors.append(i)
            n //= i
    return factors

n = int(input("请输入一个正整数："))
factors = prime_factors(n)
print(f"{n} = {' * '.join([str(x) for x in factors])}")
