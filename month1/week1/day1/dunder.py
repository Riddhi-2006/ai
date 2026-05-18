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
    def __repr__(self):
        return "Employee('{}', '{}', '{}' )".format(self.first,self.last,self.pay)
    # def __str__(self):
    #     return '{} - {}'.format(self.fullname(),self.email)
    def __add__(self, other):
        return self.pay + other.pay
    def __len__(self):
        return len(self.fullname())
        
        
        
emp1=Employee("riddhi","nashine",90000)
emp2=Employee("rohan","nandanwar",90000)
# print(emp1)
# print(emp1.__str__())
# print(emp2.__repr__())
# print(1+2)
# print(int.__add__(1,2))
# print(str.__add__('a','b'))
# print(emp1+emp2)
print(len(emp2))