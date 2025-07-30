# 12. 输入3个整数，最大公约数和最小公倍数。

a,b,c=[int(x) for x in input("请输入3个整数：").split(' ')]
gcd = a
while a % gcd != 0 or b % gcd != 0 or c % gcd != 0:
    gcd -= 1
lcm = a
while lcm % a != 0 or lcm % b != 0 or lcm % c != 0:
    lcm += a
print(f"最大公约数：{gcd}")
print(f"最小公倍数：{lcm}")
