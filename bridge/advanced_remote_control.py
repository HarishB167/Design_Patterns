from .device import Device
from .remote_control import RemoteControl

class AdvancedRemoteControl(RemoteControl):
    def __init__(self, device: Device) -> None:
        super().__init__(device)

    def setChannel(self, number: int):
        self.device.setChannel(number)
        