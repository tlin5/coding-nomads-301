# The classic OOP example: Write a class to model a car. The class should:
#
# 1. Set the attributes model, year, and max_speed in the `__init__()` method.
# 2. Have a method that increases the `max_speed` of the car by 5 when called.
# 3. Have a method that prints the details of the car.
#
# Create at least two different objects of this `Car()` class and demonstrate
# changing the objects' attributes.

class Car:

    def __init__(self, model, year, max_speed) -> None:
        self.model = model
        self.year = year
        self.max_speed = max_speed

    def newspeed(self):
        self.max_speed += 5
        return self.max_speed
    
    def detail(self):
        return f'This car model is {self.model} made in {self.year} and its max speed is {self.max_speed} miles per hour.'
    
toyota = Car('Camry', 2022, 160)
print(toyota.detail())
toyota.newspeed()
print(toyota.detail())

honda = Car('Accord', 2022, 180)
print(honda.detail())
honda.newspeed()
print(honda.detail())