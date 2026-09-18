# 作用：学习 while 循环反复输入并求平均值。
user_input = input('请输入数字（结束请按q终止程序）')
total = 0
count = 0
while user_input != 'q':
# while 作用：条件为真时循环执行，直到条件变假。
    num = float(user_input)
    total += num
    count += 1
    user_input = input('请输入数字（结束请按q终止程序）')
if count == 0 :
    result = 0
else:
    result = total/count
print('您输入的数字平均值为' + str(result))