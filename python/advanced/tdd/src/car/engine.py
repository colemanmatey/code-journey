"""
Engine class for the Car.
"""

class Engine:
    def __init__(self, type: str, horsepower: int):
        self.type = type
        self.horsepower = horsepower    

        self.validate_horsepower()

    def validate_horsepower(self):
        if not isinstance(self.horsepower, int) or self.horsepower <= 1:
            raise ValueError("Horsepower must be a positive integer or a value greater than zero")
