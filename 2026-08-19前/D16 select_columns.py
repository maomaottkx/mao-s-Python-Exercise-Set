# 作用：只查询指定两列。import os
import sqlite3
import os

script_dir = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(script_dir, 'D14 grades.db')

conn = sqlite3.connect(db_path)
cur = conn.cursor()
cur.execute('SELECT 姓名, 语文 FROM grades')
# 指定列查询：SELECT 后只写需要的列名。
for row in cur.fetchall():
   print(row)
conn.close()

