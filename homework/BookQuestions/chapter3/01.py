# 1．编写一个程序，要求完成以下要求：
# 1)	提示用户输入任意的3个小数；
# 2)	显示这三个小数；
# 3)	将这三个小数相加，并显示其结果；
# 4) 将结果按四舍五入方法转换成整数并显示。

iput_nums = [float(x) for x in input("请输入3小数：").split(' ')]
print(*iput_nums)
result = sum(iput_nums)
print(result)
print(round(result))
