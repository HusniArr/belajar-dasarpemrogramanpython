class Vehicle:
    note = "class to represent a car"

    def __init__(self):
        self.name = "common vehicle"
        self.number_of_wheels = 4

    def drive_sound(self):
        return "vroom vroooommm"
    
class ElectricCar(Vehicle):

    def __init__(self):
        Vehicle.__init__(self) #alteratif cara mengakses super class constructor
        self.name = "Electric Car" 

    def info(self):
        print(f"{self.name} has {self.number_of_wheels} wheels. engine sound: {self.drive_sound()}")

v1 = ElectricCar()
v1.info()