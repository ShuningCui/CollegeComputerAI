# 5. 编写程序，定义两个整数，用户通过键盘输入两个整数，
# 程序计算它们的和、差、积、商并输出。

input_nums = [int(x) for x in input("请输入2整数：").split(' ')]
print(*input_nums)
print(f"和：{input_nums[0] + input_nums[1]}")
print(f"差：{input_nums[0] - input_nums[1]}")
print(f"积：{input_nums[0] * input_nums[1]}")
print(f"商：{input_nums[0] / input_nums[1]}")