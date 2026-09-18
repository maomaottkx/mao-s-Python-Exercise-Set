import pandas as pd
import os
import sqlite3

script_dir = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(script_dir, 'D14 grades.db')
df = pd.read_csv(r'E:\python项目\D11 teacher_class.csv', encoding='utf-8-sig')
conn = sqlite3.connect(db_path)
df.to_sql('teacher', conn, if_exists='replace', index=False)
df = pd.read_sql_query("SELECT * FROM teacher", conn)
cursor = conn.cursor()
cursor.execute('SELECT  grades.*, teacher.班主任 FROM grades JOIN teacher ON grades.班级 = teacher.班级')
rows = cursor.fetchall()
print(rows)
cursor.fetchall()
conn.close()