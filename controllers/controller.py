from flask import render_template, request

from app import app
from models.event import Event
from models.event_list import events, add_event

@app.route("/events")
def index():
    return render_template("index.html", title="All Events", all_events=events)

@app.route("/events", methods=["POST"])
def create_event():
    event_date = request.form["date"]
    event_name = request.form["name"]
    event_guests = request.form["num_guests"]
    event_room = request.form["room"]
    event_desc = request.form["description"]
    new_event = Event(date = event_date, name = event_name, num_guests = event_guests, room = event_room, description = event_desc)
    add_event(new_event)
    return render_template("index.html", title="Home", all_events=events)
