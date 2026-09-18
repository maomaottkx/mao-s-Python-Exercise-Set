# 作用：学习用 open 读取文本文件。
with open('E:\\python项目\\No,16练习.txt','r',encoding='utf-8') as f:
# open('r') 读取模式打开文件；with 自动关闭文件。
   content = f.read()
# f.read() 读取整个文件内容。
   print(content)
