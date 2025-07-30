# 16. 计算机在教育领域的使用被称为“计算机辅助教学（CAI）” 。
# 编写程序，帮助小学生练习100以内的正整数加法。
# 程序产生2个100以内的正整数a和b，在屏幕显示a+b=?，
# 然后，学生输入答案。如答对，显示“Very Good！”，
# 并出下一道题。如错误，显示“NO”，然后让学生重新给出答案，
# 直到做对为止。要求使用一个独立的函数产生每一道题。

import random

def generate_question():
    a, b = random.randint(1, 100), random.randint(1, 100)
    print(f"{a} + {b} = ?")
    return a + b

for _ in range(10):
    result = generate_question()
    while int(input()) != result:
        print("NO")
    print("Very Good!")
