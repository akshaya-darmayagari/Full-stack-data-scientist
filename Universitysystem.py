class Professor:
    def __init__(self, name, subject):
        self.name = name
        self.subject = subject
    def teach(self, course):
        return f"{self.name} is teaching {course}"
    def give_assignment(self, task):
        return f"{self.name} assigned: {task}"
class Student:
    def __init__(self,name,courses=[],assignments=[]):
        self.name=name
        self.courses=courses
        self.assignments=assignments
    def enroll(self,course):
        self.courses.append(course)
        return f"{self.name} enrolled in {course}"
    def submit_assignment(self,task):
        self.assignments.append(task)
        return f"{self.name} submitted: {task}"
prof=Professor("Dr. Smith","Computer Science")
stud=Student("Alice")
print(prof.teach("Python"))
print(stud.enroll("Python"))    
print(prof.give_assignment("Project 1"))
print(stud.submit_assignment("Project 1"))