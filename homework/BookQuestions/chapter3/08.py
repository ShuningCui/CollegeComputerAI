# 8. 所谓孪生素数是指间隔为 2 的相邻素数，
# 例如最小的孪生素数是3和5，5和7也是。
# 找出2~200之间的孪生素数

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

for i in range(2, 200):
    if is_prime(i) and is_prime(i + 2):
        print(f"{i}和{i + 2}是孪生素数")
