# 作用：用 csv 读取成绩表并逐行显示
import csv
import os

script_dir = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(script_dir, 'D1 grades.csv')

with open(csv_path, 'r', encoding='utf-8-sig') as f:
    reader = csv.reader(f)
    # 跳过第一行表头
    next(reader)
    # 逐行读取并打印学生成绩
    for name, student_id, num1, num2, num3 in reader:
        print(f'姓名：{name},学号：{student_id},语文：{num1},数学：{num2}，英语：{num3}')
