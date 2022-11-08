# Ref : https://towardsdatascience.com/how-to-use-abstract-classes-in-python-d4d2ddc02e90
from abc import ABC, abstractmethod

from .audit_trail import AuditTrail

class Task(ABC):
    __audit_trail: AuditTrail = None

    def __init__(self, audit_trail: AuditTrail = None):
        self.__audit_trail = AuditTrail() if audit_trail is None else audit_trail

    def execute(self):
        self.__audit_trail.record()
        self._do_execute()

    @abstractmethod
    def _do_execute(self):
        pass
