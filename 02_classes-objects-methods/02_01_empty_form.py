# A good way to think about how classes are blueprints of objects is to think of
# an empty form, for example one that you would get at a doctor's office.
# The empty form contains all the placeholders that define what information
# you need to fill to complete the form. If you fill it correctly, then you've
# successfully instantiated a form object, and your completed form now holds
# information that is specific to just you.
# Another patient's form will follow the same blueprint, but hold different info.
# You could say that every patient's filled form instance is part of the same
# empty form blueprint class that the doctor's office provided.
#
# Model such an application form as a Python class below, and instantiate
# a few objects from it.


class DocApp:
    def __init__(self, first, last, reason):
        self.first = first
        self.last = last
        self.reason = reason

    def info(self):
        return f'{self.first} {self.last} is here because of {self.reason}'

i = DocApp('Bagel', 'Legal', 'Flu')
c = DocApp('Dumb', 'Dumber', 'Crazy')
print(i.info())
print(c.info())
