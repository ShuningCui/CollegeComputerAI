# P036-按规则去掉星号
# 输入字符串，字符串中有若干星号*,去掉字符串首尾的星号（*），保留中间的星号。 
# 输入：带有*号的字符串。
# 输出：首尾不带*号的字符串。
# 样例：
# ***street**music****
# street**music


string = input()
i = 0
while string[i]=='*':
    i += 1
j=len(string)-1
while string[j]=='*':
    j -= 1
print(string[i:j+1])