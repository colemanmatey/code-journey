"""
Singleton Design Pattern

The Singleton design pattern is a creational design pattern that ensures
a class has only one instance and provides a global point of access to 
that instance. This can be useful in situations where exactly one object 
is needed to coordinate actions across the system.
"""


class Singleton:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Singleton, cls).__new__(cls)

            # Configuration for the Singleton goes here.
        return cls._instance

