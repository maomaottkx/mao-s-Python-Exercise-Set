import csv
import os
# 脚本所在目录 + 数据文件名，拼出完整路径，保证从任意位置运行都能找到文件
script_dir = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(script_dir, 'D1 grades.csv')
# 空字典：之后把“姓名”当键，“该生各科成绩”当值
student_dict = {}
# 接收用户要查询的科目
query_subject = input("请输入要查询的科目（语文/数学/英语）:")

# 用户可能输入不存在的科目，先校验，避免最后取数据时报 KeyError
if query_subject not in {'语文', '数学', '英语'}:
    print("没有这个科目，请输入：语文 / 数学 / 英语")
    exit()

with open(csv_path,'r',encoding='utf-8-sig') as f:
    reader = csv.reader(f)
    next(reader)
    # D1 grades.csv 现在有 6 列：姓名、班级、学号、语文、数学、英语
    for name, class_id, student_id, num1, num2, num3 in reader:
       student_dict[name] = {'学号': student_id, '语文': int(num1), '数学': int(num2), '英语': int(num3)}

# 遍历字典，逐个打印每个学生该科目的成绩
for name, data in student_dict.items():
    print(f"{name} 的 {query_subject} 成绩是：{data[query_subject]}")
