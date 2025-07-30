# 3. 编写一个程序，将字符串“ Love”译成密码，译码方法采用替换加密法，
# 其加密规则是：将原来的字母用字母表中其后面的第 3个字母的来替换，
# 如字母 c就用 f来替换，字母 y用 b来替换。

str_code = "Love"
str_coded = [chr(ord(x) + 3) for x in str_code]
print(''.join(str_coded))
