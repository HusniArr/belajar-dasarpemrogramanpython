#Nested inheritance
class Vehicle:
    note = "class to represent a car"

    def __init__(self, name = "common vehicle", number_of_wheels = 4):
        self.name = name
        self.number_of_wheels = number_of_wheels

    def drive_sound(self):
        return "vroom vroooommm"

class Car(Vehicle):
    pass
    
class ElectricCar(Car):

    def __init__(self):
        super().__init__(name="electric car") 

    def drive_sound(self, sound="ezzzzz"):
        return ("friendly sound", sound)
    
    def info(self):
        print(f"{self.name} has {self.number_of_wheels} wheels. engine sound: {self.drive_sound()}")

v1 = Vehicle()
print(f"{v1.name} has {v1.number_of_wheels} wheels. engine sound: {v1.drive_sound()}")

v2 = Car()
v2.name = "common car"
print(f"{v2.name} has {v2.number_of_wheels} wheels. engine sound: {v2.drive_sound()}")

v3 = ElectricCar()
v3.info()