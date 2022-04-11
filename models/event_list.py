from datetime import date

from models.event import Event

event1_desc = "Farset Labs opened its doors on 6th April 2012. Let's celebrate our birthday!"
event2_desc = "Free for Farset Labs members, £3 suggested donation for non-members\n\nJoin us on the 23rd April 2022 for the first Vintage Computing Meetup at Farset Labs. Bring your own vintage computer or simply join in using one of the many on display. Make sure to register for the game competition (for bragging rights only) or simply talk to likeminded folk about your next vintage upgrade. You could even bring your hardware and upgrade it on the day! Commodore, Atari, classic IBM compatible or any vintage 80s/90s computer or games console."

event1 = Event(date(2022, 4, 9), "Farset's 10th Birthday", 30, "Main event space", event1_desc)
event2 = Event(date(2022, 4, 23), "Vintage Computing Meetup", 10, "Main event space", event2_desc)
events = [event1, event2]

def add_event(event):
    events.append(event)

def identify_event(query):
    return [event for event in events if query.casefold() in event.name.casefold()]

def delete_event(event):
    if event in events:
        events.remove(event)
