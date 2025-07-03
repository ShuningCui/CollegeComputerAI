# p020-统计其中各个英文字母的出现次数
# 输入一个可能带空格字符的字符串(长度不超过100)，统计其中各个英文字母的出现次数，
# 不区分大小写。输出字母a～z的出现次数，数据间以英文逗号分隔。非英文字母不统计。
# 输入：可能带空格的字符串。
# 输出：26个整数，以英文逗号分隔。


string = input().upper()
count = [0] * 26
for s in string:
    if s.isalpha():
        count[ord(s) - ord('A')] += 1
print(','.join([str(i) for i in count]))