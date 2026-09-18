# 作用：用 pandas 和 matplotlib 画总分柱状图和班级对比图。
import pandas as pd
import os
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']
plt.rcParams['axes.unicode_minus'] = False
script_dir = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(script_dir, 'D12 cleaned_grades.csv')
data = pd.read_csv(csv_path)
data['总分'] = data['语文'] + data['数学'] + data['英语']
data['平均分'] = data['总分'] / 3
plt.bar(data['姓名'],data['总分'])
class_group = data.groupby('班级')[['语文', '数学', '英语']].mean()
class_group.plot(kind='bar')
#DataFrame.plot(kind='bar') 直接用 pandas 画柱状图。
plt.title('各班平均分对比')
plt.xlabel("学生")
plt.ylabel('平均分')
plt.ylabel("总分")
plt.savefig('D13 班级对比.png')
plt.show()

