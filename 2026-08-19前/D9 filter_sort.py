# 作用：用布尔条件筛选行并按列排序。
import pandas as pd
df = pd.read_csv(r'E:\python项目\D1 grades.csv', encoding='utf-8-sig')
print(df[df['语文'] > 80])
# 布尔筛选：df[条件] 只保留满足条件的行。print(df.sort_values('数学', ascending=False))# sort_values() 按列排序，ascending=False 是从大到小。