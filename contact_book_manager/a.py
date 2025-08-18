class Organism:
    def __init__(self):
        print("Organism created")

class Mammal(Organism):
    def __init__(self):
        Organism.__init__(self)
        print("Mammal created")

class Human(Mammal):
    def __init__(self):
        Mammal.__init__(self)
        print("Human created")

person = Human()
