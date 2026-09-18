# 作用：读取成绩，计算总分/平均分/最高最低分，并写入 txt 报告
import csv  # 处理 csv 表格文件
import os  # 拼接文件路径

script_dir = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(script_dir, 'D1 grades.csv')

with open(csv_path, 'r', encoding='utf-8-sig') as f:
    reader = csv.reader(f)
    next(reader)  # 跳过表头行
    for name, student_id, num1, num2, num3 in reader:
        mark_list = [int(num1), int(num2), int(num3)]
        # 组合统计：把三科成绩转成 list 后，用 max/min/sorted 计算
        print(f'{name}同学，你的总分是{int(num1) + int(num2) + int(num3)}')
        print(f'你的平均分是{(int(num1) + int(num2) + int(num3)) / 3}')
        print(f'你的最高分是{max(mark_list)}')
        print(f'你的最低分是{min(mark_list)}')
        print(f'由低到高分别为{sorted(mark_list)}')
        with open('E:/python项目/D3 analysis_report.txt', 'a', encoding='utf-8-sig') as r:
            # 写入报告：追加模式把统计结果保存到 txt
            r.write(f'{name}同学，你的总分是{int(num1) + int(num2) + int(num3)}')
            r.write(f'\n你的平均分是{(int(num1) + int(num2) + int(num3))/3}')
            r.write(f'\n你的最高分是{max(mark_list)}')
            r.write(f'\n你的最低分是{min(mark_list)}')
            r.write(f'\n由低到高分别为{sorted(mark_list)}\n')
