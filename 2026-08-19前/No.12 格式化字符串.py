# 两个列表分别存放姓名和成绩
name = ['may', 'jack']
mark = ['95', '90']

# append()：在列表末尾追加一个元素
name.append('nan')
mark.append('99')

# zip()：把两个列表按下标一一配对，n 取姓名，m 取成绩
for n, m in zip(name, mark):
    # f-string：用 {} 把变量值直接嵌入字符串
    student_mark = f'{n},{m}'
    print(student_mark)
