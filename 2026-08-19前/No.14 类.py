# 作用：学习用 class 定义类，封装属性和方法。
class student :
# class 作用：定义类，用来创建对象。
   def __init__(self,name,student_id) :
# __init__ 作用：创建对象时自动初始化属性；self 代表当前对象。
        self.name = name
        self.student_id = student_id
        self.grades = {'语文':0, '数学':0, '英语':0}
   def set_grade(self, course, grade) :
# 实例方法：创建对象后可以调用，操作该对象自己的数据。
        if course in self.grades :
            self.grades[course] = grade
   def print_grade(self) :
        print(f'学生 ；{self.name}(学号：{self.student_id})的成绩为{self.grades}')
        for course in self.grades:
            print(f'{course}:{self.grades[course]}')



chen = student('陈','070110')
chen.set_grade('语文','122')
chen.set_grade('数学','79')
chen.set_grade('英语','91')
chen.print_grade()