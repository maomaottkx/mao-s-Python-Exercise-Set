# 作用：处理缺失值：求平均、删除空行、用 0 或平均值填补。
import pandas as pd
data = pd.read_csv(r'E:\python项目\D12 missing.csv', encoding='utf-8-sig')
print(data)
print(data['语文'].mean())
# mean() 求一列平均值，自动跳过空值。
print(data.dropna())
# dropna() 删除含空值的行。
print(data.fillna(0))
# fillna() 把空值替换成指定值或列平均值。
print(data.fillna(data[['语文', '英语']].mean()))