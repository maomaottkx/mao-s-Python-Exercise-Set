# 作用：int(input(...)) 把输入的文字转成整数再存进变量
mood_index = int(input('对象今天的心情指数'))
# 作用：if 条件成立就执行缩进的代码块，否则执行 else 的代码块
if mood_index <= 60:
    # 作用：嵌套 if，先满足外层条件才会执行到这里
    is_at_home = str(input('她在家吗'))
    if is_at_home == 'yes':
        print('NO')
    else:
        print('OK')
else:
    print('OK')
