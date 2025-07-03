# P044-删除字符串中所有非小写字母字符
# 输入一个英文字符串（长度<81）可能包含空格，删除其中所有非小写字母的字符，
# 并输出删除后的字符串（小写字母的相对位置保持不变）。
# 样例：
# A# 7b
# b



string = input()
lower = [s for s in string if s.islower()]
print(''.join(lower))