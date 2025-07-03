# P035-单词加密问题
# 单词加密。输入一个字符串和一个非负整数k，对字符串中的每一个字母，
# 用字母表中其后的第k个字母代替，不够k个时再从字母a循环计数。
# 例如k=3是，a用d代替，A用D代替，x用a代替，y用b代替，保持大小写不变。
# 字符串中的非字母字符不变。字符串的长度不超过100。
# 输入：一个字符串（无空格）和非负整数k，之间用空格分隔
# 输出：加密的字符串。



def encoder(x,n):
    base = 65 if x.isupper() else 97
    return chr(base+(ord(x)-base+n)%26)

string, str_n = input().split()
n = int(str_n)%26
print(''.join([encoder(x,n) if x.isalpha() else x for x in string ]))