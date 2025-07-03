# P040-将字符串首部的*号全部移到字符串的尾部
# 将字符串首部的*号全部移到字符串的尾部，中间若有*号，
# 保持中间的*号不动。字符串长度不超过200.
# 样例：
# ***street*****music***
# street*****music******


string = input()
i = 0
while string[i]=='*':
    i += 1
print(string[i:]+string[:i])