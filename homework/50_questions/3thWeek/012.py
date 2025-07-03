# P012-判断一个正整数是否为回文数
# 编写一个函数来判断一个正整数是否为回文数，若是则返回1，否则返回0。
# 所谓回文数是指各位数字左右对称的数，例如1221、3553等。该函数的原型为： 
# def ispalindrome(n): 
# 其中参数n是待判断的正整数，若是，该函数返回True，反之返回False。
# 使用该函数找出1000∽n (包括1000和n,1000 ≤ n <10000)之间的所有回文数，
# 按从小到大的次序在屏幕上显示输出，每个数之间用一个空格分隔，最后一个数后面没有空格。



def ispalindrome(n):
    return str(n) == str(n)[::-1]

n = int(input())
ispalindrome_number = []
for i in range(1000, n+1):
    if ispalindrome(i):
        ispalindrome_number.append(i)
print(*ispalindrome_number)