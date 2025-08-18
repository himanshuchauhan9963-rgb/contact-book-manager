class Student:
    def __init__(self, name, roll_number, marks):
        self.name = name
        self.roll_number = roll_number
        self.marks = marks

    def display(self):
        print(f"Name: {self.name}, Roll No: {self.roll_number}, Marks: {self.marks}")

# Creating two student objects
student1 = Student("Gaurav", 17, 87.5)
student2 = Student("Himanshu", 102, 92.0)


student1.display()
student2.display()
