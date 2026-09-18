# 作用：学习用 def 定义函数并返回结果。
def colculate_BMI(weight, height):
    # def 作用：定义函数，把代码封装成可重复调用的单元。
    BMI = weight / height ** 2
    if BMI <= 18.5:
        category = '偏瘦'
    elif 18.5 < BMI <= 25:
        category = '正常'
    elif 25 < BMI <= 30:
        category = '偏胖'
    else:
        category = "肥胖"
    print(f'您的BMI分类为{category}')
    return BMI
# return 作用：把函数计算结果返回给调用位置。
colculate_BMI(66, 1.6)