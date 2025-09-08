class Employee:
    def __init__(self,name,salary,role):
        self.name=name
        self.salary=salary
        self.role=role
    def bonus(self):
        if(self.role=="Manager"):
            return self.salary*0.2
        elif(self.role=="Developer"):
            return self.salary*0.1
        elif(self.role=="Intern"):
            return self.salary*0.05
e=Employee("TOM",50000,"Manager")
print(e.bonus())