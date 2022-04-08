from datetime import date

from models.event import Event

event1 = Event(date(2022, 4, 9), "Farset Labs turns 10", 30, "Main event space", "Farset Labs opened its doors on 6th April 2012. Let's celebrate our birthday!")
events = [event1]

def add_event(event):
    events.append(event)
