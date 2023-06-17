from .calendar import Calendar
from .scheduler import Scheduler
from .arabian_calendar import ArabianCalendar

class ArabianScheduler(Scheduler):

    def get_calendar(self) -> Calendar:
        return ArabianCalendar()
        
