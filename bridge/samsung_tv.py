from .device import Device

class SamsungTV(Device):

    def turnOn(self):
        print("Samsung: turnOn")

    def turnOff(self):
        print("Samsung: turnOff")

    def setChannel(self, number: int):
        print("Samsung: setChannel")
        