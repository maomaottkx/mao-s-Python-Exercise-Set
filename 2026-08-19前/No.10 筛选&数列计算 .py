# 作用：学习 range 和 for 循环累加 1 到 100。
temperature_list = {'111':37.5,'222':36.8,'333':37.0}
for staff_id,temperature in temperature_list.items():
     if temperature > 37.3:
        print(staff_id)
total = 0
for num in range(1, 101,):
# range() 生成连续整数；for 循环逐个取出并执行循环体。
   total += num
   print(total)

