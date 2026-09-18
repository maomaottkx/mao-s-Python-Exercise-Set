# 作用：按班级分组计算各科平均分。
import pandas as pd

df = pd.read_csv(r'E:\python项目\D1 grades.csv', encoding='utf-8-sig')
print(df.groupby('班级')[['语文', '数学', '英语']].mean())
# groupby('班级')[列].mean()：按班级分组后对各科求平均。
