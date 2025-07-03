# P009-翻译数字
# 编写一个程序，从键盘上读入一个数字串，把数字转化为对应的小写英语数字单词输出。
# 例如：输入234，输出two three four。
# 输入：一串数字
# 输出：用空格隔开英文数字单词（英文字母都是小写）。
# 样例：
# 234
# two three four

num = [int(x) for x in input()]
english = ['zero','one','two','three','four','five','six','seven','eight','nine']
out = [english[n] for n in num] 
print(*out)