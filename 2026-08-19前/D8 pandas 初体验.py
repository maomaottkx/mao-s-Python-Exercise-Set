# 作用：首次使用 pandas，读取 CSV 并查看基本信息。
import pandas as pd
# pandas 模块：数据分析库，pd 是常用别名。
df = pd.read_csv(r'E:\python项目\D1 grades.csv', encoding='utf-8-sig')
pd.read_csv() 
# 读取 CSV，生成 DataFrame 表格。print(df)
print(df.head())
# head() 查看前几行。
print(df.info())
# info() 查看每列类型和非空数量。
print(df.describe())# describe() 生成数值列统计摘要。