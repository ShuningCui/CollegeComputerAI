# P038-按规则删除星号
# 编写程序，删除字符串中间的所有星号*，如果首尾有*号，保留不变。字符串长度不超过200。
# 如：输入***street*****music***，则输出***streetmusic***
# 输入：带*号的字符串（字符串中不含空格）。
# 输出：中间没有*号的字符串。


string = input()
i = 0
while string[i]=='*':
    i += 1
j=len(string)-1
while string[j]=='*':
    j -= 1
print(string[:i]+string[i:j+1].replace('*','')+string[j+1:])