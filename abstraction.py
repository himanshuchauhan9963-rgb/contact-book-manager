from abc import ABC, abstractmethod

# Abstract class
class SmartDevice(ABC):
    def __init__(self):
        self.status = "OFF"

    @abstractmethod
    def turn_on(self):
        pass

    @abstractmethod
    def turn_off(self):
        pass

    @abstractmethod
    def get_status(self):
        pass


# Concrete class: SmartLight
class SmartLight(SmartDevice):
    def __init__(self):
        super().__init__()
        self.brightness = 50

    def turn_on(self):
        self.status = "ON"
        self.brightness = 50

    def turn_off(self):
        self.status = "OFF"
        self.brightness = 0

    def get_status(self):
        return f"Light is {self.status}, Brightness: {self.brightness}"


# Concrete class: SmartThermostat
class SmartThermostat(SmartDevice):
    def __init__(self):
        super().__init__()
        self.temperature = 22  # Default temperature

    def turn_on(self):
        self.status = "ON"

    def turn_off(self):
        self.status = "OFF"

    def get_status(self):
        return f"Thermostat is {self.status}, Temperature: {self.temperature}°C"


# Concrete class: SmartSpeaker
class SmartSpeaker(SmartDevice):
    def __init__(self):
        super().__init__()
        self.volume = 5
        self.track = "None"

    def turn_on(self):
        self.status = "ON"
        self.track = "Playing Jazz"
        self.volume = 7

    def turn_off(self):
        self.status = "OFF"
        self.track = "None"
        self.volume = 0

    def get_status(self):
        return f"Speaker is {self.status}, Volume: {self.volume}, Track: {self.track}"


# Function to summarize devices
def device_summary(devices: list[SmartDevice]):
    for device in devices:
        device.turn_on()
    print("\nStatus after turning ON:")
    for device in devices:
        print(device.get_status())

    for device in devices:
        device.turn_off()
    print("\nStatus after turning OFF:")
    for device in devices:
        print(device.get_status())


# Client code
if __name__ == "__main__":
    light = SmartLight()
    thermostat = SmartThermostat()
    speaker = SmartSpeaker()

    all_devices = [light, thermostat, speaker]
    device_summary(all_devices)
