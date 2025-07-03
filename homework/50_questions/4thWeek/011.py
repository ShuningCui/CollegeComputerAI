# P011-找出m到n之间的所有同构数
# 找出整数m到整数n (闭区间）之间的所有同构数（m<n）。
# 说明：一个正整数x，如果是它平方数的尾部，则称x为同构数。
# 例如，6是其平方数36的尾部，25是其平方数625的尾部，那么6和25都是同构数。
# 输入：m和n两个正整数，用空格分隔。
# 输出：连续输出同构数，数据间用空格分隔(最后一个同构数后面无空格)。


input = [int(i) for i in input().split()]
isomorphic_number = []
for x in range(input[0], input[1] + 1):
    if str(x*x).endswith(str(x)):
        isomorphic_number.append(x)
print(*isomorphic_number)
