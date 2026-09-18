# 作用：练习：输入两科成绩，计算总分平均分并判断及格。
num1 = int(input('请输入语文成绩：'))
num2 = int(input('请输入数学成绩：'))
print(num1 + num2)
print((num1 + num2)/2)
if num1 >= 60:
    print('语文及格')
else:
    print('语文不及格')
if num2 >= 60:
    print('数学及格')
else:
    print('数学不及格')
