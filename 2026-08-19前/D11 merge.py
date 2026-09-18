# 作用：读取成绩表与班主任表，合并后生成班级平均分透视表。
import os
import pandas as pd

script_dir = os.path.dirname(os.path.abspath(__file__))
grades_path = os.path.join(script_dir, 'D1 grades.csv')
teacher_path = os.path.join(script_dir, 'D11 teacher_class.csv')

grades = pd.read_csv(grades_path, encoding='utf-8-sig')
teachers = pd.read_csv(teacher_path, encoding='utf-8-sig')
teachers = teachers.drop_duplicates()
# drop_duplicates() 删除重复行。
# pd.merge() 按 on 列横向合并两个表。
merged = pd.merge(grades, teachers, on='班级')
print(merged)
# pivot_table() 生成透视表，按“班级”分组，对三门课求平均分。
pivot = merged.pivot_table(index='班级', values=['语文', '数学', '英语'], aggfunc='mean')
print(pivot)
