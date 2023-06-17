from datetime import datetime

from .event import Event
from .calendar import Calendar

class GregorianCalendar(Calendar):

    def add_event(self, event: Event, date: datetime):
        print("Adding an event on the given date in Gregorian Calendar.")