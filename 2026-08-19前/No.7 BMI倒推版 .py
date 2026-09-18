# 作用：用 BMI 公式反推体重，练习变量运算和类型转换。
user_height = float(input('请输入你的身高（单位是米）:'))
user_BMI = 20
user_weight  = user_BMI * user_height ** 2
# 变量运算：把计算公式的结果保存进变量，之后可以继续使用。
print(int(user_weight))
