class Shape:
    def __init__(self,name):
        self.name=name
    def area(self):
        pass
class Circle(Shape):
    def __init__(self,name,radius):
        super().__init__(name)
        self.radius=radius
    def area(self):
        return 3.14*self.radius*self.radius
class Rectangle(Shape):
    def __init__(self,name,length,breadth):
        super().__init__(name)
        self.length=length
        self.breadth=breadth
    def area(self):
        return self.length*self.breadth
c=Circle("Circle",5)
print(c.name,":",c.area())
r=Rectangle("Rectangle",4,6)
print(r.name,":",r.area())
