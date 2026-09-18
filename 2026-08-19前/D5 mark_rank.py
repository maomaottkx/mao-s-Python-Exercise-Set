import csv      # 导入 csv 模块，用于读写 CSV 文件
import os       # 导入 os 模块，用于拼接文件路径

# 获取当前脚本所在目录，并拼接出成绩文件路径
script_dir = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(script_dir, 'D1 grades.csv')

with open(csv_path,'r',encoding='utf-8-sig') as f:
    reader = csv.reader(f)      # 创建 CSV 读取器
    next(reader)                # 跳过表头行
    avg_list = []               # 用来保存（姓名, 总分）的列表，需放在循环外
    # 当前表格有 6 列：姓名、班级、学号、语文、数学、英语
    for name,class_id,student_id,num1,num2,num3 in reader:
        total_mark = int(num1) + int(num2) + int(num3)   # 计算总分
        avg_list.append((name,total_mark))               # 把结果加入列表
    print(sorted(avg_list))      # 按总分从小到大排序并打印
