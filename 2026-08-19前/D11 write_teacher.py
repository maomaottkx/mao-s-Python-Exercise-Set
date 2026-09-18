# 作用：把班级和班主任对应关系写入 teacher CSV，空文件自动补表头。
# zip() 把两个列表“配对”，csv.writer 把每对数据写成一行。
import csv
import os
script_dir = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(script_dir, 'D11 teacher_class.csv')
name = ['王老师', '李老师']
teacher_class = ['1', '2']

file_empty = not os.path.exists(csv_path) or os.path.getsize(csv_path) == 0

with open(csv_path, 'a', newline='', encoding='utf-8-sig') as csv_file:
    write = csv.writer(csv_file)
    if file_empty:
        write.writerow(['班级', '班主任'])
    for t_class, t_name in zip(teacher_class, name):
        write.writerow([t_class, t_name])

