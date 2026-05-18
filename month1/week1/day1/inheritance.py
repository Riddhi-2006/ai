class Employee:
    raise_amt = 1.94
    def __init__(self,first,last,pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@gmail.com'
    def fullname(self):
        return '{} {}'.format(self.first,self.last)
    def apply_raise(self):
        self.pay=int(self.pay * self.raise_amt)

class Developer(Employee):
    raise_amt = 1.1
    def __init__(self,first,last,pay,prog_lang):
        super().__init__(first,last,pay)
        # Employee.__init__(self,first,last,pay)
        self.prog_lang = prog_lang

class Manager(Employee):
    def __init__(self,first,last,pay,employees=None):
        super().__init__(first,last,pay)
        if employees is None:
            self.employees = []
        else :
            self.employees = employees
    def add_emp(self,emp):
        if emp not in self.employees :
            self.employees.append(emp)
    def remove_emp(self,emp):
        if emp in self.employees :
            self.employees.remove(emp)
    def print_emps(self):
        for emp in self.employees :
            print("-->",emp.fullname())        


dev_1 = Developer("riddhi","nashine",900000,'python')
dev_2 = Employee("rohan","nandanwar",90000)
# print(dev_1.email)
# print(help(Developer))
# print(dev_1.pay)
# print(dev_2.pay)
# dev_1.apply_raise()
# print(dev_1.pay)
print(dev_1.__dict__)
mngr_1 = Manager("Riddhi", "Nashine",100000,[dev_1,dev_2])
print(mngr_1.email)
mngr_1.print_emps()
print(isinstance(mngr_1,Manager))
print(issubclass(Manager,Employee))