"""
The Builder Design Pattern

The Builder Design Pattern is a creational design pattern that provides a way
to construct a complex object step by step. It allows you to create different 
representations of an object using the same construction process. This pattern 
is particularly useful when an object has a large number of parameters or 
configurations, and you want to create different variations of the object without 
exposing its internal representation.
"""


class Computer:
    def __init__(self):
        self.cpu = None
        self.gpu = None
        self.ram = None
        self.psu = None
        self.hdd = None

    def __str__(self):
        return f"Specification\n{'-'*13}\nCPU: {self.cpu}\nGPU: {self.gpu}\nRAM: {self.ram}\nPSU: {self.psu}\nStorage: {self.hdd}"
    

class ComputerBuilder:
    def __init__(self):
        self.computer = Computer()

    def set_cpu(self, cpu):
        self.computer.cpu = cpu
        return self
    
    def set_gpu(self, gpu):
        self.computer.gpu = gpu
        return self
    
    def set_ram(self, ram):
        self.computer.ram = ram
        return self
    
    def set_psu(self, psu):
        self.computer.psu = psu
        return self
    
    def set_hdd(self, hdd):
        self.computer.hdd = hdd
        return self
    
    def build(self):
        return self.computer
        

builder = (
    ComputerBuilder()
        .set_cpu("Intel Core i9")
        .set_gpu("Nvidia GeForce RTX 4090")
        .set_hdd("Seagate BarraCuda 1TB")
        .set_ram("G.Skill Trident Z5 Neo RGB DDR5-6000 (2 x 16GB)")
        .set_psu("Cooler Master V750 Gold V2")
)


computer = builder.build()

print(computer)