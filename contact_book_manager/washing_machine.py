# Base class
class Appliance:
    def __init__(self, power_rating):
        self.power_rating = power_rating

# Child class
class WashingMachine(Appliance):
    def __init__(self, power_rating, capacity):
        # Manually calling base class constructor without using super()
        Appliance.__init__(self, power_rating)
        self.capacity = capacity

    def display(self):
        print(f"Power Rating: {self.power_rating} Watts")
        print(f"Capacity: {self.capacity} kg")

# Create a WashingMachine object
wm = WashingMachine(1200, 7)

# Display the object’s attributes
wm.display()
