# P043-将整数分解为1和各个质因子的相乘
# 从键盘输入一个正整数（>1)，然后将该整数分解为1和各个质因子的相乘，
# 如果输入的整数本身就是质数，则应分解为1和该数本身相乘。
# 18
# 1*2*3*3


n = int(input())
prime_factor = [1]
f=2
while n>1:
    if n%f==0:
        prime_factor.append(f)
        n//=f
    else:
        f+=1
print('*'.join(str(p) for p in prime_factor))
