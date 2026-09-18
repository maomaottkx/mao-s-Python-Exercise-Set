# NO.6：BMI 多条件判断，示范 if / elif / else 的分支写法
user_weight = float(input('请输入你的体重（单位是千克）: '))
user_height = float(input('请输入你的身高（单位是米）:'))
# 已修复：先计算 BMI，再打印；原代码把变量名写进了引号
user_BMI = user_weight / user_height ** 2
# ** 是幂运算，user_height ** 2 表示身高的平方
print("你的BMI是" + str(user_BMI))
# if / elif / else：从上到下匹配第一个成立的条件，只执行一个分支
if user_BMI <= 18.5:
    print('偏瘦')
elif 18.5 < user_BMI <= 25:
    print('正常')
elif 25 < user_BMI <= 30:
    print('偏胖')
else:
    print("肥胖")