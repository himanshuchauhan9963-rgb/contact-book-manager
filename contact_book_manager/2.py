class Shape:
    def draw(self):
        print("Drawing a shape")

class Circle(Shape):
    def draw(self):
        print("Drawing a circle")

class Rectangle(Shape):
    def draw(self):
        print("Drawing a rectangle")

class Triangle(Shape):
    def draw(self):
        print("Drawing a triangle")

# Polymorphism in action
shapes = [Circle(), Rectangle(), Triangle()]

for shape in shapes:
    shape.draw()  # Calls appropriate overridden method
    '''Python uses dynamic method resolution.

Even though each object is of type Shape, the correct method (draw()) from the respective subclass is called.

No if or type() checks were needed — that’s true polymorphism.'''
