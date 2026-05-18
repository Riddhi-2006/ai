class Employee:
    def __init__(self,first ,last, pay):
        self.first=first
        self.last=last
        self.pay=pay
        self.email= first +'.'+ last +'@company.com'
    def fullname(self):
        return '{} {}'.format(self.first,self.last)
emp1=Employee("riddhi","nashine",90000)
emp2=Employee("rohan","nandanwar",90000)
print(emp1)
print(emp2)
print(emp1.email)
print(emp2.email)
print(emp1.fullname())
print(emp2.fullname())
print(Employee.fullname(emp1))
print(emp1.__dict__)
print(emp2.__dict__)
print(Employee.__dict__)

class Student:
    def __init__(self, name, cgpa):
        self.name = name
        self.cgpa = cgpa

    def introduce(self):
        print(f"I'm {self.name} with CGPA {self.cgpa}")

s = Student("Riddhi", 9.5)
s.introduce()