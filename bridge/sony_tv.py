from .device import Device

class SonyTV(Device):

    def turnOn(self):
        print("Sony: turnOn")

    def turnOff(self):
        print("Sony: turnOff")

    def setChannel(self, number: int):
        print("Sony: setChannel")
        