# P034-和差积商
# 输入2个整数，求：和，差，积，商
# 输入：2个整数（第二个数是非零整数）
# 输出：4个整数，依次为和、差、积和商，数据间用空格分隔。


num = [int(x) for x in input().split()]
a,b = num[0],num[1]
print(a+b,a-b,a*b,a/b)
