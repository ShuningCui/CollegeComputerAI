# P028-找到连续出现最多的字符
# 编写程序，要求在一个字符串中查找连续出现次数最多的一个字符，
# 并显示其所在的开始下标和次数。(如果出现最多的字符不止一个，输出最靠前的字符)
# 输入：一个字符串（无空格）
# 输出：出现最多的字符，次数，开始索引（这三个值之间用空格分隔，末尾无空格）



string = input()
count=i=start_index=0

while i < len(string)-1:
    count_current = 1
    start_index_current = i
    while i < len(string)-1 and string[i]==string[i+1]:
        count_current += 1
        i += 1
    if count_current > count:
        count = count_current
        start_index = start_index_current
    i += 1
print(string[start_index],count,start_index)