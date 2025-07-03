# P007-学生成绩排序
# 有n名学生，每个学生的数据包含学号、姓名、三门课的成绩。
# 可以从键盘输入n个学生的数据，按总成绩从小到大排序，
# 打印包含学号、姓名、三门课成绩和总成绩的成绩单。（测试时，数据从键盘输入。）
# 输入：第1行为整数n，后面n行表示n个人的信息，包括学号、姓名、和三门课的成绩，每行的数据间用空格隔开。
# 输出：n行，表示n个人的信息，包括学号、姓名、三门课的成绩和总成绩，数据间一个空格，末尾无空格。
# 样例：
# 输入：
# 2
# 2021001 li 60 80 70
# 2021002 wang 100 90 80
# 输出：
# 2021001 li 60 70 80 210
# 2021002 wang 100 90 80 270

n = int(input())
student_list = []
for i in range(n):
    student_list.append(input().split())
    student_list[i].append(sum([int(x) for x in student_list[i][-3:]]))
student_list.sort(key=lambda x: x[-1])
for student in student_list:
    print(*student)