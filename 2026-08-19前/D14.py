# 用途：学生成绩管理系统，支持录入、查看、统计、查询和图表展示
import csv
import pandas as pd
import os
import matplotlib.pyplot as plt

# 设置中文字体，防止图表里的中文变成方块
plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']
plt.rcParams['axes.unicode_minus'] = False
# __file__ 是当前文件路径，os.path.dirname 取它所在的文件夹
script_dir = os.path.dirname(os.path.abspath(__file__))
# os.path.join 把文件夹和文件名拼成一个完整路径
csv_path = os.path.join(script_dir, 'D14 grades.csv')

# 根据用户输入的数字进入不同功能模块
while True:
    action = input('1. 录入学生  2. 查看成绩 3. 统计分析 4. 查询学生成绩 5. 查看图表 6.退出:')
    if action not in ('1', '2', '3', '4', '5', '6'):
        print('请输入1~6的数字')
        continue

    # 后面的功能都要读成绩文件，文件为空时先提示录入
    if action in ('2', '3', '4', '5') and (not os.path.exists(csv_path) or os.path.getsize(csv_path) == 0):
        print('请先录入成绩数据')
        continue

    if action == '1':
       name = input('姓名:')
       student_class = input('班级:')
       student_id = input('学号:')
       try:
          num1 = int(input('请输入语文成绩：'))
          num2 = int(input('请输入数学成绩：'))
          num3 = int(input('请输入英语成绩：'))
       except ValueError:
          print('请输入合理数字')
       else:
          if num1 > 100 or num2 > 100 or num3 > 100 or num1 < 0 or num2 < 0 or num3 < 0:
              print('请输入0~100的数字')
          else:
              # 文件不存在或为空时先写入表头，再追加学生数据
              file_empty = not os.path.exists(csv_path) or os.path.getsize(csv_path) == 0
              with open(csv_path, 'a', newline='', encoding='utf-8-sig') as f:
                  write = csv.writer(f)
                  if file_empty:
                      write.writerow(['姓名', '班级', '学号', '语文', '数学', '英语'])
                  write.writerow([name, student_class, student_id, num1, num2, num3])
                  print(f'成绩已保存到: {csv_path}')



    if action == '2':
       if os.path.exists(csv_path) and os.path.getsize(csv_path) > 0:
           df = pd.read_csv(csv_path, encoding='utf-8-sig')  # 用和写入时一致的编码读取，避免乱码
           df = df.drop_duplicates()
           df.to_csv(csv_path, index=False, encoding='utf-8-sig')
           teachers = pd.read_csv(os.path.join(script_dir, 'D11 teacher_class.csv'), encoding='utf-8-sig')
           teachers = teachers.drop_duplicates()
           # 按班级合并班主任信息，先统一成字符串类型，否则 int 和 str 无法匹配
           df['班级'] = df['班级'].astype(str)
           teachers['班级'] = teachers['班级'].astype(str)
           df = pd.merge(df, teachers, on='班级')
           class_avg = df.groupby('班级')[['语文', '数学', '英语']].mean()
           print(class_avg.round(2))
           print(df)



    if action == '3':
        if os.path.exists(csv_path) and os.path.getsize(csv_path) > 0:
           df = pd.read_csv(csv_path, encoding='utf-8-sig')
           df = df.drop_duplicates()
           df.to_csv(csv_path, index=False, encoding='utf-8-sig')
        # 计算总分和平均分
        df['总分'] = df['英语'] + df['语文'] + df['数学']
        df['平均分'] = df[['语文', '数学', '英语']].mean(axis=1)
        print(df[['姓名', '总分', '平均分']])
        # 按总分从高到低排序
        print(df.sort_values('总分', ascending=False)[['姓名', '总分', '平均分']])
        print(df[['语文', '数学', '英语', '总分', '平均分']].describe())
        # 达标名单
        print(df[df['总分'] >= 240][['姓名', '总分']])
        # 不及格名单
        print(df[df['总分'] < 240][['姓名', '总分']])



    if action == '4':
        if os.path.exists(csv_path) and os.path.getsize(csv_path) > 0:
            df = pd.read_csv(csv_path, encoding='utf-8-sig')
            df = df.drop_duplicates()
            df.to_csv(csv_path, index=False, encoding='utf-8-sig')
        name = input("请输入学生姓名：")
        # 按姓名精确筛选，找到就显示，找不到提示
        result = df[df['姓名'] == name]
        if result.empty:
            print("没有找到该学生")
        else:
            print(result)
    if action == '5':
        if os.path.exists(csv_path) and os.path.getsize(csv_path) > 0:
            df = pd.read_csv(csv_path, encoding='utf-8-sig')
            df = df.drop_duplicates()
            df.to_csv(csv_path, index=False, encoding='utf-8-sig')
            df['总分'] = df['语文'] + df['数学'] + df['英语']
            # 总分排名图
            plt.bar(df['姓名'], df['总分'])
            plt.title("学生分数排名")
            plt.xlabel("学生")
            plt.ylabel("总分")
            plt.savefig(os.path.join(script_dir, 'D14 总分排名.png'))
            plt.show()
            # 班级平均分对比图
            # 新建一张画布，避免总分图和班级对比图叠在同一张图里
            plt.figure()
            class_group = df.groupby('班级')[['语文', '数学', '英语']].mean()
            class_group.plot(kind='bar')
            plt.title('各班平均分对比')
            plt.xlabel("班级")
            plt.ylabel('平均分')
            plt.savefig(os.path.join(script_dir, 'D14 班级平均分对比.png'))
            plt.show()
    if action == '6':
        print('已退出')
        break