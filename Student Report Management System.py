import csv
import os

# Constants
FILE_NAME = "student_records.csv"

# ------------------- Student Class -------------------
class Student:
    def __init__(self, roll_number, name, age, grade):
        self.roll_number = roll_number
        self.name = name
        self.age = age
        self.grade = grade

    def __str__(self):
        return f"{self.roll_number}, {self.name}, {self.age}, {self.grade}"


# ------------------- Student Manager -------------------
class StudentManager:
    def __init__(self):
        self.students = []
        self.load_from_file()

    def load_from_file(self):
        if not os.path.exists(FILE_NAME):
            return
        try:
            with open(FILE_NAME, mode='r', newline='') as file:
                reader = csv.reader(file)
                for row in reader:
                    if row:
                        roll_number, name, age, grade = row
                        self.students.append(Student(roll_number, name, age, grade))
        except Exception as e:
            print(f"Error loading file: {e}")

    def save_to_file(self):
        try:
            with open(FILE_NAME, mode='w', newline='') as file:
                writer = csv.writer(file)
                for student in self.students:
                    writer.writerow([student.roll_number, student.name, student.age, student.grade])
        except Exception as e:
            print(f"Error saving file: {e}")

    def add_student(self):
        roll_number = input("Enter Roll Number: ")
        if not roll_number.isdigit():
            print("Roll Number must be numeric!")
            return
        if self.find_student_by_roll(roll_number):
            print("Student with this Roll Number already exists!")
            return
        name = input("Enter Name: ")
        age = input("Enter Age: ")
        grade = input("Enter Grade: ")
        self.students.append(Student(roll_number, name, age, grade))
        self.save_to_file()
        print("Student added successfully.")

    def view_all_students(self):
        if not self.students:
            print("No student records found.")
            return
        self.students.sort(key=lambda x: x.roll_number)
        print("All Student Records:")
        for student in self.students:
            print(student)

    def find_student_by_roll(self, roll_number):
        for student in self.students:
            if student.roll_number == roll_number:
                return student
        return None

    def search_student(self):
        roll_number = input("Enter Roll Number to search: ")
        student = self.find_student_by_roll(roll_number)
        if student:
            print("Student Found:", student)
        else:
            print("Student not found.")

    def update_student(self):
        roll_number = input("Enter Roll Number to update: ")
        student = self.find_student_by_roll(roll_number)
        if not student:
            print("Student not found.")
            return
        print("Leave blank to keep existing value.")
        name = input(f"Enter New Name [{student.name}]: ") or student.name
        age = input(f"Enter New Age [{student.age}]: ") or student.age
        grade = input(f"Enter New Grade [{student.grade}]: ") or student.grade
        student.name, student.age, student.grade = name, age, grade
        self.save_to_file()
        print("Student updated successfully.")

    def delete_student(self):
        roll_number = input("Enter Roll Number to delete: ")
        student = self.find_student_by_roll(roll_number)
        if not student:
            print("Student not found.")
            return
        self.students.remove(student)
        self.save_to_file()
        print("Student deleted successfully.")


# ------------------- CLI Menu -------------------
def menu():
    manager = StudentManager()
    while True:
        print("\n------ Student Report Management System ------")
        print("1. Add Student")
        print("2. View All Students")
        print("3. Search Student by Roll Number")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Exit")
        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            manager.add_student()
        elif choice == '2':
            manager.view_all_students()
        elif choice == '3':
            manager.search_student()
        elif choice == '4':
            manager.update_student()
        elif choice == '5':
            manager.delete_student()
        elif choice == '6':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

# ------------------- Main Execution -------------------
if __name__ == "__main__":
    menu()
