# 作用：把 SQL 查询结果直接转成 DataFrame。
import sqlite3
import os
import pandas as pd

script_dir = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(script_dir, 'D14 grades.db')

conn = sqlite3.connect(db_path)
df = pd.read_sql_query("SELECT * FROM grades", conn)
# pd.read_sql_query() 执行 SQL 并返回 DataFrame。
conn.close()

print(df)