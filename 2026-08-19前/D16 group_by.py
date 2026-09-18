# 作用：按班级分组计算各科平均分。
import sqlite3
import os

script_dir = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(script_dir, 'D14 grades.db')

conn = sqlite3.connect(db_path)
cursor = conn.cursor()
cursor.execute("SELECT 班级, AVG(语文), AVG(数学), AVG(英语) FROM grades GROUP BY 班级")
# GROUP BY 分组；AVG() 求平均。
for row in cursor.fetchall():
    print(row)
conn.close()