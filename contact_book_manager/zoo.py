class Animal:
    def make_sound(self):
        print("Animal")

class Lion(Animal):
    def make_sound(self):
        print("sound 1")
class Snake(Animal):
    def make_sound(self):
        print("sound 2")
    
def sounds(animals):
    for i in animals:
        i.make_sound()

zoo = [Lion(), Snake(), Lion(), Lion()]

sounds(zoo)


"""Question 2 """

class Shape:
    def draw(self):
        print("shape")

class Circle(Shape):
    def draw(self):
        print("circle")

class Rectangle(Shape):
    def draw(self):
        print("rectangle")

class Canvas:
    def __init__(self):
        self.shapes = []

    def add_shape(self, shape):
        self.shapes.append(shape)

    def render_all(self):
        for shape in self.shapes:
            shape.draw()


canvas = Canvas()
canvas.add_shape(Circle())
canvas.add_shape(Rectangle())
canvas.render_all()



"""Question 3"""

class Employee:
    def calculate_salary(self):
        pass

class FullTimeEmployee(Employee):
    def calculate_salary(self):
        return 100000

class PartTimeEmployee(Employee):
    def calculate_salary(self):
        return 60000

def process_payroll(employees):
    for i in employees:
        print(f"Salary: {i.calculate_salary()}")

team = [FullTimeEmployee(), PartTimeEmployee(), FullTimeEmployee()]
process_payroll(team)


"""Question 4"""

class Vehicle:
    def fuel_efficiency(self):
        return 0

class Car(Vehicle):
    def fuel_efficiency(self):
        return 25

class Truck(Vehicle):
    def fuel_efficiency(self):
        return 15

def efficient(vehicles):
    best = max(vehicles, key=lambda v: v.fuel_efficiency())
    print(f"Most efficient vehicle has {best.fuel_efficiency()} mpg")

vehicles = [Car(), Truck(), Car()]
efficient(vehicles)

"""Question 5"""

class Report:
    def generate(self):
        pass

class PDFReport(Report):
    def generate(self):
        print("PDF_report")

class ExcelReport(Report):
    def generate(self):
        print("Excel_report")

class HTMLReport(Report):
    def generate(self):
        print("HTML_report")

class ReportManager:
    def __init__(self, reports):
        self.reports = reports

    def generate_all(self):
        for report in self.reports:
            report.generate()

reports = [PDFReport(), ExcelReport(), HTMLReport()]
manager = ReportManager(reports)
manager.generate_all()

"""Question 6"""

class Character:
    def attack(self):
        pass

class Warrior(Character):
    def attack(self):
        print("sword")

class Archer(Character):
    def attack(self):
        print("arrow")

class Mage(Character):
    def attack(self):
        print("fireball")

def a(team):
    for character in team:
        character.attack()

b = [Warrior(), Archer(), Mage()]
a(b)



