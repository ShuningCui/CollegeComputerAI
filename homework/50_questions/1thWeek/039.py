# P039-时、分、秒转换
# 输入总秒数，转换为相应的时、分、秒。
# 输入：整数
# 输出：时分秒，整数，西文冒号分隔
# 样例
# 输入：3661
# 输出：1:01:01
# 格式提示：
# print(f'{hours}:{minutes:0>2}:{seconds:0>2}')


total_seconds = int(input())
hours = total_seconds//3600
minutes = (total_seconds%3600)//60    
seconds = total_seconds%60
print(f'{hours}:{minutes:0>2}:{seconds:0>2}')
