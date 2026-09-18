# 作用：把 CSV 导入 SQLite 数据库。
import os
import sqlite3
# sqlite3 模块：Python 内置轻量数据库。
import pandas as pd

script_dir = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(script_dir, 'D14 grades.csv')
db_path = os.path.join(script_dir, 'D14 grades.db')

df = pd.read_csv(csv_path, encoding='utf-8-sig')
conn = sqlite3.connect(db_path)
# connect() 连接数据库文件。
df.to_sql('grades', conn, if_exists='replace', index=False)
# to_sql() 把 DataFrame 写入数据库表，if_exists='replace' 覆盖旧表。
conn.close()
print('导入完成，共', len(df), '行')