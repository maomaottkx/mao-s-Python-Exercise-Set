# 作用：学习继承：子类复用父类并扩展属性。
class employee:
    def __init__(self,name,employee_id):
        self.name = name
        self.employee_id = employee_id
    def print_employee(self):
        print(f'姓名：{self.name},工号：{self.employee_id}')
class Full_Time_Employee(employee):
# 继承作用：类名括号里写父类名，子类拥有父类的方法。
    def __init__(self,month_salary, name, employee_id):
        super().__init__(name,employee_id)
# super() 作用：调用父类的方法，先完成父类初始化。
        self.month_salary = month_salary
    def calculate_employee(self):
        return self.month_salary
class Part_Time_Employee(employee):
    def __init__(self, daily_salary,work_days, name, employee_id):
        super().__init__(name, employee_id)
        self.daily_salary = daily_salary
        self.work_days = work_days
    def calculate_daily_salary(self):
        return int(self.daily_salary) * int(self.work_days)
shen = Full_Time_Employee('5000','chen','10000')
cheng = Part_Time_Employee('100','30','cheng','10003')
shen.print_employee()
cheng.print_employee()
print(shen.calculate_employee())
print(cheng.calculate_daily_salary())
