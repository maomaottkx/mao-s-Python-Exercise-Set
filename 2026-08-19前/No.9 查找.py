# 作用：学习字典 dict 的查找和成员判断。
dictionary = {'dare': 'v.敢于做...;n.挑战;激将', 'print': 'v.打印'}
# dict 作用：用 {键: 值} 保存数据，按键快速查值。
dictionary['run'] = 'v.跑'#这是提醒你怎么添加的，别优化！！！
Q = input('请输入您想要查询的单词')
if Q in dictionary:
# 成员判断：in 检查键是否存在字典中。
    print('单词' + Q + '释义如下')
    print(dictionary[Q])
else:
    print('您查询的单词未收录')
    print('当前词典内词条数为' + str(len(dictionary)) + '条')

