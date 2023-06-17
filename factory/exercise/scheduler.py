from datetime import datetime

from .calendar import Calendar
from .event import Event
from .gregorian_calendar import GregorianCalendar


class Scheduler:
    __calendar: Calendar = None

    def schedule(self, event: Event):
        today = datetime.now()
        self.__calendar = self.get_calendar()
        self.__calendar.add_event(event, today)

    def get_calendar(self) -> Calendar:
        return GregorianCalendar()
