from .remote_control import RemoteControl
from .advanced_remote_control import AdvancedRemoteControl
from .sony_tv import SonyTV
from .samsung_tv import SamsungTV

if __name__ == "__main__":
    remote_control = AdvancedRemoteControl(SamsungTV())
    remote_control.turnOn()

