# 作用：录入学生成绩，空文件自动补表头，之后追加写入 CSV
# csv：CSV 表格文件的读写工具
import csv
# os：文件路径拼接与文件信息判断
import os

# 脚本所在文件夹，保证不管从哪里运行都能找到数据文件
script_dir = os.path.dirname(os.path.abspath(__file__))
# 拼接出完整的 CSV 文件路径
csv_path = os.path.join(script_dir, 'D1 grades.csv')

# input：接收键盘输入，返回字符串
name = input('姓名:')
student_class = input('班级:')
student_id = input('学号:')

try:
    # int()：把字符串转换成可计算的整数
    num1 = int(input('请输入语文成绩：'))
    num2 = int(input('请输入数学成绩：'))
    num3 = int(input('请输入英语成绩：'))
except ValueError:
    # except：输入的不是数字时执行这里
    print('请输入合理数字')
else:
    # if/else：条件判断，检查成绩是否在 0~100 范围内
    if num1 > 100 or num2 > 100 or num3 > 100 or num1 < 0 or num2 < 0 or num3 < 0:
        print('请输入0~100的数字')
    else:
        # 打印总分和平均分
        print(num1 + num2 + num3)
        print((num1 + num2 + num3) / 3)
        # 判断文件不存在或为空，决定是否要写表头
        file_empty = not os.path.exists(csv_path) or os.path.getsize(csv_path) == 0
        # with：打开文件，结束时自动关闭；'a' 是追加模式
        with open(csv_path, 'a', newline='', encoding='utf-8-sig') as f:
            # csv.writer：把列表写成表格的一行
            write = csv.writer(f)
            if file_empty:
                write.writerow(['姓名', '班级', '学号', '语文', '数学', '英语'])
            write.writerow([name, student_class, student_id, num1, num2, num3])
            print(f'成绩已保存到: {csv_path}')
