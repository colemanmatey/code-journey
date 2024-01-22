"""
The decorator design pattern is a structural pattern that allows behavior 
to be added to an individual object, either statically or dynamically, 
without affecting the behavior of other objects from the same class. 
It is often used to extend or modify the behavior of functions or methods.
"""

# Step 1: Define the core component (function)
def core_function():
    print("This is the core functionality.")

# Step 2: Define decorators
def decorator1(func):
    def wrapper():
        print("Decorator 1 - Before core function")
        func()
        print("Decorator 1 - After core function")

    return wrapper

def decorator2(func):
    def wrapper():
        print("Decorator 2 - Before core function")
        func()
        print("Decorator 2 - After core function")

    return wrapper

# Step 3: Apply decorators to the core component
# Method 1
core_function = decorator1(core_function)
core_function = decorator2(core_function)

# Method 2
@decorator1
@decorator2
def core_function():
    print("This is the core functionality.")

# Step 4: Call the enhanced core component
core_function()
