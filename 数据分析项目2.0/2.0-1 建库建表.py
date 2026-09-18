import sqlite3
import pandas as pd
import os
conn = sqlite3.connect('grades.db')   # 文件不存在会自动创建
cur = conn.cursor()                    # 游标 = 执行 SQL 的"手"
cur.execute('''CREATE TABLE IF NOT EXISTS grades (
    姓名 TEXT,
    班级 INTEGER,
    学号 INTEGER,
    语文 INTEGER,
    数学 INTEGER,
    英语 INTEGER
)''')
script_dir = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(script_dir,  '..', '2026-08-19前', 'D14 grades.csv')
df = pd.read_csv(csv_path,encoding='utf-8-sig')
data = df.values.tolist()   # 每一行变成一个元组 (姓名, 班级, 学号, 语文, 数学, 英语)
cur.executemany('INSERT INTO grades VALUES (?, ?, ?, ?, ?, ?)', data)
for row in cur.execute('SELECT * FROM grades'):
    print(row)
conn.commit()   # ← 最容易忘的一步！不 commit，关程序数据就没了
conn.close()