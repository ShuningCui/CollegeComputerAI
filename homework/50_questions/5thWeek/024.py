# P024-统计字母次数
# 输入一个可能含空格的字符串，分别统计其中26个英文字母出现的次数
# （不区分大、小写字母），并按字母出现的次数，从高到低进行排序。
# 若次数相同，按字母顺序排列。字母输出格式举例，
# 例如：A-3，表示字母A出现3次，C-0表示字母C没有出现过。
# 输入：
# 第一行为输入，占一行
# 输出：
# 第二行为输出，占一行。按照字母输出格式从高到低输出，各字母输出之间用一个空格字符进行分隔。
# 样例：
# 123abcAABXxwvUu+
# A-3 B-2 U-2 X-2 C-1 V-1 W-1 D-0 E-0 F-0 G-0 H-0 I-0 J-0 K-0 L-0 M-0 N-0 O-0 P-0 Q-0 R-0 S-0 T-0 Y-0 Z-0


string = [s for s in input().upper() if s.isalpha()]
count = []
for i in range(26):
    count.append((chr(65+i),string.count(chr(65+i))))
count.sort(key=lambda x:x[1],reverse=True)
out = [f'{s[0]}-{s[1]}' for s in count]
print(*out)