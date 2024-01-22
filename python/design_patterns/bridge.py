"""
The Bridge design pattern

The Bridge design pattern is a structural pattern that decouples an abstraction 
from its implementation so that the two can vary independently. This pattern 
involves creating a bridge interface, containing a reference to the implementer 
interface. By doing this, the abstraction and implementation can evolve 
independently without affecting each other.
"""

# Implementer Interface
class Device:
    def turn_on(self):
        pass

    def turn_off(self):
        pass

# Concrete Implementers
class TV(Device):
    def turn_on(self):
        print("Turning on the TV")

    def turn_off(self):
        print("Turning off the TV")

class Radio(Device):
    def turn_on(self):
        print("Turning on the Radio")

    def turn_off(self):
        print("Turning off the Radio")

# Abstraction Interface
class RemoteControl:
    def __init__(self, device):
        self.device = device

    def turn_on(self):
        self.device.turn_on()

    def turn_off(self):
        self.device.turn_off()

# Refined Abstractions
class BasicRemote(RemoteControl):
    pass

class AdvancedRemote(RemoteControl):
    def mute(self):
        print("Muting the device")

# Usage
tv = TV()
radio = Radio()

basic_remote_tv = BasicRemote(tv)
basic_remote_tv.turn_on()
basic_remote_tv.turn_off()

basic_remote_radio = BasicRemote(radio)
basic_remote_radio.turn_on()
basic_remote_radio.turn_off()

advanced_remote_tv = AdvancedRemote(tv)
advanced_remote_tv.turn_on()
advanced_remote_tv.turn_off()
advanced_remote_tv.mute()

advanced_remote_radio = AdvancedRemote(radio)
advanced_remote_radio.turn_on()
advanced_remote_radio.turn_off()
advanced_remote_radio.mute()
