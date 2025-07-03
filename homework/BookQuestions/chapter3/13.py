# 13. 读入5个用户的姓名和电话号码，
# 按姓名的字典顺序排列后，输出用户的姓名和电话号码。

name_num_list = []
for i in range(5):
    name, phone = input("请输入姓名和电话号码：").split(' ')
    name_num_list.append((name, phone))
name_num_list.sort()
for name, phone in name_num_list:
    print(f"{name}: {phone}")
