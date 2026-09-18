# 用途：读取成绩 CSV，输入姓名即可查询该同学的全部资料
import csv
import os
script_dir = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(script_dir, 'D1 grades.csv')
with open(csv_path,'r',encoding='utf-8-sig') as f:
    reader = csv.reader(f)
    next(reader)
    student_data = {}
    # 逐行读取，把“姓名 -> 完整资料”存进字典
    for name, class_id, student_id, num1, num2, num3 in reader:
        student_data[name] = f'班级: {class_id}, 学号: {student_id}, 语文: {num1}, 数学: {num2}, 英语: {num3}'
# 输入姓名后直接查字典；找不到就提示
Q = input('请输入姓名:')
if Q in student_data:
    print(student_data[Q])
else:
    print("系统中无信息")
