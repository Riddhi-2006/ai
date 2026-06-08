class Friends :
    def __init__(self,name,surname,how,status):
        self.name = name
        self.surname = surname
        self.how = how
        self.status = status
    def fullname(self):
        return '{} {}'.format(self.name,self.surname)
frnd1 = Friends('Rohan','Nandanwar','college','Boyfriend/Bestfriend')
frnd2 = Friends('shruti','dhole','college','friend')
print(frnd1)
print(frnd1.__dict__)
print(frnd1.fullname())
