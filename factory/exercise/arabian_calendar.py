from datetime import datetime

from .event import Event
from .calendar import Calendar

class ArabianCalendar(Calendar):

    def add_event(self, event: Event, date: datetime):
        print("Adding an event on the given date in Arabian Calendar.")