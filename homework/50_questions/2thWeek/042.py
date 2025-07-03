# P042-检验由三边能否构成三角形
# 编写程序检验由三边能否构成三角形，检验方法是任意两边和均要大于第三边。
# 输入:三边长度（一行输入，空格分隔）
# 输出：如果可以构成三角形，输出YES，否则输出ERROR DATA


def is_triangle(a, b, c):
    return a + b > c and a + c > b and b + c > a

input = [float(x) for x in input().split()]
if is_triangle(input[0], input[1], input[2]):
    print("YES")
else:
    print("ERROR DATA")

