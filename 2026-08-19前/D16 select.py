# 作用：用 SQL 查询全部数据。
import os
import sqlite3

script_dir = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(script_dir, 'D14 grades.db')

conn = sqlite3.connect(db_path)
cur = conn.cursor()
# cursor() 创建游标，用于执行 SQL 并取结果。
cur.execute('SELECT * FROM grades')
# SELECT *：查询所有列；execute() 执行 SQL。
for row in cur.fetchall():
# fetchall() 取出所有结果行。
    print(row)
    conn.close()