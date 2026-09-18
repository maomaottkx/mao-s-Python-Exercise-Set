#BMI指数
# 作用：float(input(...)) 把用户输入的文字转成小数再存进变量
user_weight = float(input("请输入你的体重（单位是千克）: "))
user_height = float(input('请输入你的身高（单位是米）:'))
# 作用：按 BMI = 体重 / 身高² 计算，** 2 表示平方
user_BMI = user_weight / user_height ** 2
# 复习：str() 把数字转成字符串，才能用 + 和文字拼接输出
print("你的BMI是" + str(user_BMI))
