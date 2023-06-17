from .event import Event
from .scheduler import Scheduler
from .arabian_scheduler import ArabianScheduler

if __name__ == "__main__":

    scheduler = Scheduler()
    scheduler.schedule(Event())

    arabian_scheduler = ArabianScheduler()
    arabian_scheduler.schedule(Event())
     