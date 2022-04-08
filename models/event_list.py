from models.event import Event

event1 = Event("someDate", "eventName", 40, "roomLoc", "eventDesc")
events = [event1]

def add_event(event):
    events.append(event)
