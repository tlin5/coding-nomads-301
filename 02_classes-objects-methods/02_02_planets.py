# Create a `Planet()` class that models attributes and methods of
# a planet object.
# Use the appropriate dunder method to get informative output with `print()`

class Planet:
    def __init__(self, planet, color) -> None:
        self.planet = planet
        self.color = color

    def planetcolor(self):
        return f'Plaent {self.planet} is {self.color}'

    # def __str__(self) -> str:
    #     return f'{self.planet} - {self.color}'
    
    def __repr__(self) -> str:
        return f'planet = {self.planet} \ncolor = {self.color}'

e = Planet('earth' , 'blue')
print(e.planetcolor())
print(e)
print(repr(e))

