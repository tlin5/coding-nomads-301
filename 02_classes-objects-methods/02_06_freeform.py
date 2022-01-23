# Write a script with three classes that model everyday objects.
# - Each class should have an `__init__()` method that sets at least 3 attributes
# - Include a `__str__()` method in each class that prints out the attributes
#     in a nicely formatted string.
# - Overload the `__add__()` method in one of the classes so that it's possible
#     to add attributes of two instances of that class using the `+` operator.
# - Create at least two instances of each class.
# - Once the objects are created, change some of their attribute values.
#
# Be creative. Have some fun. :)
# Using objects you can model anything you want:
# Animals, paintings, card games, sports teams, trees, people etc...

class Gun:

    def __init__(self, model, round, chamber):
        self.model = model
        self.round = round
        self.chamber = chamber

    def __add__(self, other):
        other.current_round -= 1
        self.chamber = 1
        self.round = other.current_round
        return Gun(self.model, self.round, self.chamber)
    
    def __str__(self):
        return f'This gun model is {self.model} with {self.round} round loaded and {self.chamber} round in the chamber.'

class Magazine:

    def __init__(self, magazine_size, model, current_round):
        self.magazine_size = magazine_size
        self.model = model
        self.current_round = current_round
    
    def __add__(self, other):
        """This is add func is for magazine and ammo"""
        self.current_round += self.magazine_size
        other.ammo_count -= self.magazine_size
        return Magazine(self.magazine_size, self.model, self.current_round)

    def __str__(self):
        return f'This magazine can hold {self.magazine_size} round of ammo. It is for {self.model} gun. This magazine currently has {self.current_round} round.'

class Ammo:

    def __init__(self, ammo_count, caliber, type):
        self.ammo_count = ammo_count
        self.caliber = caliber
        self.type = type

    def __str__(self):
        return f'There are {self.ammo_count} rounds of ammo. The caliber of the round is {self.caliber}. The type of ammo is {self.type}'
    
if __name__ == '__main__':
    g = Gun('HK416', 30, 0)
    m = Magazine(30, 'HK 416 Magazine', 0)
    a = Ammo(210, 5.56, 'm855')

    l1 = m + a
    l2 = g + m

    print(l1)
    print(l2)