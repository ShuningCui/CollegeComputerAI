# P017-删除串中的重复字符
# 输入一个字符串，删除串中的重复字符。
# 输入：要检查的字符串 例如：abacaeedabcdcd。
# 输出：  删除重复字符后的字符串。例如：abced。


out=""
for s in input():
    if s not in out:
        out+=s
print(out)
