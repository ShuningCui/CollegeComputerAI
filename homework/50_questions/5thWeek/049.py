# P049-按ASCII排序输出字符串
# 输入两个字符串s, t，(字符串中没有空格，包含大小写字母、数字以及其他符号）
# 按从小到大顺序输出在s或t中出现过(不区分大小写)的所有字符，所有字母均按大写输出
# 重复的字符只输出1次。
# 输入：1行，两个字符串中间用空格隔开，字符串不含空格
# 输出：结果字符串，按ASCII编码从小到大排序。

 
input = input().split()
str1 = input[0].upper()
str2 = input[1].upper()
str3 = []
for s in str1:
    if s not in str3:
        str3.append(s)
for s in str2:
    if s not in str3:
        str3.append(s)
str3.sort()
print(''.join(str3))
