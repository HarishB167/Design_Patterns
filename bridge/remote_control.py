from .device import Device

class RemoteControl:
    def __init__(self, device: Device) -> None:
        self.device: Device = device

    def turnOn(self):
        self.device.turnOn()

    def turnOff(self):
        self.device.turnOff()
        