class X:
    def execute(self):
        print("X executed")

class Y:
    def execute(self):
        print("Y executed")

class Z(X, Y):
    def execute(self):
        print("Z executed")

class Final(Z):
    def run(self):
        self.execute()

f = Final()
f.run()  # Output: Z executed
'''In Python, when you call a method on an object that comes from a class with multiple inheritance, Python uses something called the Method Resolution Order (MRO) to decide which method to run. The MRO is just the order in which Python looks through the classes to find the method. For example, in the class Final that inherits from Z, which itself inherits from both X and Y, the MRO is: Final → Z → X → Y → object. This means Python first checks Final, then Z, then X, and finally Y. If the Z class has its own execute() method, Python finds it there and uses it. But if Z doesn't have execute(), Python continues searching in the order of the MRO and finds execute() in X before reaching Y, so X's method is used. This behavior shows how Python supports multiple inheritance and resolves conflicts by following a fixed search order, ensuring consistent and predictable method execution.

'''
