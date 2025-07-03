# P031-按规则输出倒序字符串
# 编写程序，按下列规则倒序输出子字符串。先输出最后的一个字符，
# 再输出最后两个字符串，在再出后面三个字符..., 最后输出整个字符串。输入的字符串长度不超过100。
# 输入：一个字符串（无空格，字符个数不超过100）
# 输出：空格隔开的子字符串，用一个空格间隔。
# 样例：
# student
# t nt ent dent udent tudent student


string = input()
out = [string[-i:] for i in range(1, len(string)+1)]
print(*out)