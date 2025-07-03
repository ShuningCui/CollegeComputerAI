# P003-去掉一个字符串中除头部和尾部空格外的所有空格
# 去掉一个字符串中除头部和尾部空格外的所有空格。
# 样例：
#    abc  de
#    abcde


string = input()
# Found the first character that is not a space
i = 0
while string[i] == " ":
    i += 1
# Found the last character that is not a space
j = len(string) - 1
while string[j] == " ":
    j -= 1
# Print the string with spaces removed
print(string[:i] + string[i:j+1].replace(" ", "") + string[j+1:])
