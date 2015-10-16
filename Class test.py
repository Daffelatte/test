__author__ = 'olof.olivecrona'

# synax
# class className(Self, Classes that the class inherits from):
#   __init__(self, argument):
#
class dog(object):
    def __init__(self, name, race):
        self.name=name
        self.race=race
    def bark(self):
        if self.race =="pudel":
            return "viff!"
        elif self.race =="shepherd":
            return "VOFF!!"

dog1 = dog(name="Molly",race="pudel")
dog2 = dog(name="Bruno", race="shepherd")

print dog1.bark()
print dog2.bark()
