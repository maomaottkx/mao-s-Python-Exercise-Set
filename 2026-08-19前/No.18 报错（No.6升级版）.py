# 作用：学习 try/except 处理错误。try:
try:#尝试执行；except 捕获错误；else 无错误时执行。
   user_weight = float(input('请输入你的体重（单位是千克）: '))
   user_height = float(input('请输入你的身高（单位是米）:'))
   user_BMI = user_weight / user_height ** 2
except ValueError:
    print('请输入合理数字')
except ZeroDivisionError:
    print('身高不可为零')
except:
    print('发生未知错误，请重新输入')
else:
    print(user_BMI)
    print("你的BMI是" + str(user_BMI))
    if user_BMI <= 18.5:
        print('偏瘦')
    elif 18.5 < user_BMI <= 25:
        print('正常')
    elif 25 < user_BMI <= 30:
        print('偏胖')
    else:
        print("肥胖")