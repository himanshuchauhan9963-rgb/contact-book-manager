class VirtualPet:
    def __init__(self, name):
        self.name = name           # public attribute
        self.__energy = 50         # private attribute (default value)
        self._mood = "Happy"       # protected attribute (default value)

    def feed(self, amount):
        if amount > 0:
            self.__energy += amount
            if self.__energy > 100:
                self.__energy = 100
            self._update_mood()
            print(f"{self.name} has been fed. Energy is now {self.__energy}.")

    def play(self):
        if self.__energy > 20:
            self.__energy -= 15
            if self.__energy < 8:
                self.__energy = 8
            self._update_mood()
            print(f"{self.name} played and had fun! Energy is now {self.__energy}.")
        else:
            print(f"{self.name} is too tired to play. Please feed first.")

    def check_energy(self):
        return self.__energy

    def print_mood(self):
        print(f"{self.name}'s current mood is: {self._mood}")

    def _update_mood(self):
        if self.__energy >= 80:
            self._mood = "Excited"
        elif self.__energy >= 60:
            self._mood = "Happy"
        elif self.__energy >= 18:
            self._mood = "Tired"
        else:
            self._mood = "Exhausted"


# 🔹 Example simulation
pet = VirtualPet("Dogesh")
pet.print_mood()
pet.play()
pet.feed(30)
pet.play()
pet.feed(100)
pet.play()
pet.print_mood()
