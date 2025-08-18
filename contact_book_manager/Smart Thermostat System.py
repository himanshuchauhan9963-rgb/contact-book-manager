class Thermostat:
    def __init__(self):
        self.__temperature = 22  # default safe temperature

    def increase_temperature(self):
        if self.__temperature < 30:
            self.__temperature += 1
        else:
            print("⚠️ Temperature can't go above 30°C. Keeping last valid value.")

    def decrease_temperature(self):
        if self.__temperature > 16:
            self.__temperature -= 1
        else:
            print("⚠️ Temperature can't go below 16°C. Keeping last valid value.")

    def show_temperature(self):
        print(f"🌡️ Current temperature is: {self.__temperature}°C")


# ✅ Demo of Thermostat
t = Thermostat()
t.show_temperature()
t.increase_temperature()
t.increase_temperature()
t.show_temperature()

# Test edge cases
for _ in range(15):
    t.decrease_temperature()
t.show_temperature()

for _ in range(20):
    t.increase_temperature()
t.show_temperature()
