# 作用：用 WHERE 条件筛选行。
import os
import sqlite3

script_dir = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(script_dir, 'D14 grades.db')

conn = sqlite3.connect(db_path)
cur = conn.cursor()
cur.execute('SELECT 姓名, 语文 FROM grades WHERE 语文 >= 80')
# WHERE 只返回满足条件的行。
for row in cur.fetchall():
    print(row)
conn.close()