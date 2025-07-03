# 2. 键盘输入任意三个整数，然后输出这三个数并计算其平均值。

iput_nums = [int(x) for x in input("请输入3整数：").split(' ')]
print(*iput_nums)
print(sum(iput_nums) / 3)