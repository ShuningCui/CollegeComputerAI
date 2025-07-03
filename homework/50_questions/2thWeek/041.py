# P041-计算银行存款本息
# 计算银行存款本息。输入存款金额money（单位：元），存期years，
# 年利率rate，计算到期存款本息（保留2位小数）。计算公式如下：
# sum=money*((1+rate)^years)
# 输入:存款金额，存期，年利率。均为浮点数，且用逗号分隔
# 输出：存款本息（保留2位小数）


input = [float(x) for x in input().split(',')]
sum = input[0]*(1+input[2])**input[1]
print(f'{sum:.2f}')
