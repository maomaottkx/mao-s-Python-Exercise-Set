# 作用：学习用 open 的 w/a 模式写文件和追加内容。
with open('E:\\python项目\\No.17练习.txt','w',encoding='utf-8') as f:
# open('w') 会清空原文件后重新写入；f.write() 写入文字。
    f.write('Hi')
with open('E:\\python项目\\No.17练习.txt','a',encoding='utf-8') as f:
    f.write('\nHi')
with open('E:\\python项目\\No.17练习.txt','a',encoding='utf-8') as f:
# open('a') 追加模式，在文件末尾继续添加内容。    f.write('\n你好')
    f.write('\n你好')
with open('E:\\python项目\\No.17练习.txt','r',encoding='utf-8') as f:
    content = f.read()
    print(content)
