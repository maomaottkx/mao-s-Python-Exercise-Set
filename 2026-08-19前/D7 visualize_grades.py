import matplotlib.pyplot as plt  # 导入绘图库，并给它起短名 plt
import csv
import os

# 让图表里的中文能正常显示
plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']
# 让负号正常显示（不用 Unicode 的负号）
plt.rcParams['axes.unicode_minus'] = False

# __file__ 是当前文件路径，os.path.dirname 取它所在的文件夹
script_dir = os.path.dirname(os.path.abspath(__file__))
# os.path.join 把文件夹和文件名拼成一个完整路径
csv_path = os.path.join(script_dir, 'D1 grades.csv')

# 先检查文件是否存在且不是空文件，避免后面 next(reader) 报错
if not os.path.exists(csv_path) or os.path.getsize(csv_path) == 0:
    print("找不到 D1 grades.csv 或文件为空，无法画图。")
    exit()

with open(csv_path, 'r', encoding='utf-8-sig') as f:
    reader = csv.reader(f)
    next(reader)  # 跳过表头行
    total_mark_list = []
    name_list = []
    for name, class_id, student_id, num1, num2, num3 in reader:
        total_mark = int(num1) + int(num2) + int(num3)  # 字符串转整数再求和
        total_mark_list.append(total_mark)
        name_list.append(name)

# 一个学生都没有时，不要画空图
if not name_list:
    print("表格里没有任何学生数据，无法画图。")
    exit()

plt.bar(name_list, total_mark_list)  # 柱状图：横轴是姓名，竖轴是总分
plt.title("学生分数排名")
plt.xlabel("学生")
plt.ylabel("总分")
plt.savefig('D7 总分排名.png')  # 把图片保存成文件
plt.show()  # 弹出窗口显示图片
