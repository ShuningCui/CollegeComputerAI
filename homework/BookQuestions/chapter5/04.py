# 4. 输入一个总的秒数，将该秒数换算为相应的时、分、秒。
# 如输入3600秒，则输出结果为1小时，输入3610秒，
# 则结果为1小时10秒，通过除法和求余运算完成。

total_seconds = int(input("请输入总秒数："))
hours = total_seconds // 3600
minutes = (total_seconds % 3600) // 60
seconds = total_seconds % 60
print(f"{hours}小时{minutes}分{seconds}秒")