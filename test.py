#
# Example file for working with classes
# LinkedIn Learning Python course by Joe Marini
#

# BASE CLASS
class Vehicle():
    def __init__(self, bodystyle):
        self.bodystyle = bodystyle

    def drive(self, speed):
        self.mode = "driving"
        self.speed = speed

# VEHICLE SUB CLASS
class Car(Vehicle):
    def __init__(self, enginetype):
        super().__init__("Car")
        self.wheels = 4
        self.doors = 4
        self.enginetype = enginetype

    def drive(self, speed):
        super().drive(speed)
        print("Driving my", self.enginetype, "car at", self.speed)

# MOTORCYCLE SUB CLASS
class Motorcycle(Vehicle):
    def __init__(self, enginetype, hassidecar):
        super().__init__("Motorcyle")
        if(hassidecar):
            self.wheels = 3
        else:
            self.wheels = 2
        # WHAT THE SPACING HERE, the following two lines are separate from the else!!
        self.doors = 0
        self.enginetype = enginetype

    def drive(self, speed):
        super().drive(speed)
        print("Driving my", self.enginetype, "motorcycle at", self.speed)

# MY VEHICLES
car1 = Car("gas")
car2 = Car("electric")
car3 = Car("gas")
mc1 = Motorcycle("gas", True)

print(mc1.wheels)
print(car1.enginetype)
print(car2.doors)

car1.drive(30)
car2.drive(40)
mc1.drive(50)