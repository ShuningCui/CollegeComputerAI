# P050-除首尾字符外降序排序
# 输入一个字符串（不包含空格，至少有1个字符），除首尾字符外，
# 将其余的字符按ascii码降序排列，然后输出。


string = input()
if len(string) == 1:
    print(string)
    exit()
str1 = list(string[1:-1])
str1.sort(reverse=True)
print(string[0]+''.join(str1)+string[-1])

