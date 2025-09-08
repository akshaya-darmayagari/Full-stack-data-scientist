class Student_Average:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
    def average(self):
        return sum(self.marks) / len(self.marks)
    def add_mark(self, mark):
        self.marks.append(mark)
    def get_highest(self):
        return max(self.marks)
    def get_lowest(self):
        return min(self.marks)
Stu=Student_Average("Sri",[90,85,80])
print(Stu.average())
Stu.add_mark(95)
print(Stu.get_highest())
print(Stu.get_lowest())