# P006-电话簿排序
# 编写一个程序，读入n个用户姓名和电话号码，按姓名的字典顺序排列后，
# 输出用户的姓名和电话号码，n从键盘输入。
# 样例：
# 输入：
# 
# 3
# zhang 122
# wang 233
# li 567
# 输出：
# li 567
# wang 233
# zhang 122


n = int(input())
phone_list = []
for _ in range(n):
    phone_list.append(input())
phone_list.sort()
for phone in phone_list:
    print(phone)
