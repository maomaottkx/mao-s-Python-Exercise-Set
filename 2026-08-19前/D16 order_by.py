# 作用：按总分从高到低排序。
import sqlite3
import os

script_dir = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(script_dir, 'D14 grades.db')

conn = sqlite3.connect(db_path)
cursor = conn.cursor()
cursor.execute("SELECT 姓名, 语文+数学+英语 AS 总分 FROM grades ORDER BY 总分 DESC")
# AS 给计算结果起别名；ORDER BY 排序；DESC 从高到低。
for row in cursor.fetchall():
    print(row)
conn.close()