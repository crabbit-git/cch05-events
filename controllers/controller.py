from flask import render_template

from app import app
from models.event import Event
from models.event_list import events

@app.route("/events")
def index():
    return render_template("index.html", title="All Events", all_events=events)
