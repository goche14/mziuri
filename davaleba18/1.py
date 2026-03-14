class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

student1 = Student("gio", 8)
student2 = Student("luka", 9)

print(student1.name, student1.grade)
print(student2.name, student2.grade)

student1.grade += 5

print(student1.name, student1.grade)
print(student2.name, student2.grade)