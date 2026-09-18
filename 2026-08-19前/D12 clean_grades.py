# 作用：读取成绩表，把成绩列转成整数并保存清洗后的 CSV。
import pandas as pd
data = pd.read_csv('D1 grades.csv', encoding='utf-8-sig')
print('原始数据：')
print(data)
print('重复行数量：')
print(data.duplicated().sum())
data = data.drop_duplicates()
print('去重后：')
print(data)
print('空值数量：')
print(data.isnull().sum())
import pandas as pd
import os
script_dir = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(script_dir, 'D1 grades.csv')
data = pd.read_csv(csv_path)
data['语文'] = data['语文'].astype(int)
# astype(int) 把整列转成整数类型。
data['数学'] = data['数学'].astype(int)
data['英语'] = data['英语'].astype(int)
print(data)
print(data.dtypes)
# dtypes 查看每列数据类型。
data.to_csv('D12 cleaned_grades.csv', index=False)
#to_csv() 保存 CSV，index=False 不保存行号。