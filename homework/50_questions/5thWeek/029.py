# P029-闰年计算
# 闰年计算。程序输入一个正整数Y，以及另一个正整数N，以一个空格分隔。计算从Y年开始后的第N个闰年是哪一年（如果Y本身是闰年，则Y之后的第一个闰年是Y，闰年不超过6240年）。
# 输入格式：两个整数：Y和N。用空格分隔
# 输出个数：一个整数



def is_leap(year):
    return (year % 4 == 0 and year % 100 != 0) or year % 400 == 0

year = [int(x) for x in input().split()]
count = 0
while count<year[1]:
    if is_leap(year[0]):
        count += 1
    year[0] += 1
print(year[0]-1)