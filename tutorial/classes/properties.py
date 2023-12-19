"""
Properties
"""


class Person:

    def __init__(self, name, age):
        self._name = name
        self._age = age

    @property
    def name(self):
        return self._name * 3
    
    @name.setter
    def name(self, value):
        self._name = value.upper()
        raise Exception("Cannot change name!")


person = Person("Cole", 28)
print(person.name)

person.name = "Mildred"
print(person.name)
