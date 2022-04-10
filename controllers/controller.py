from flask import render_template, request

from app import app
from models.eventdeets import events
from models.event import Event

@app.route('/events')
def index():

    return render_template("index.html", title="Events", all_events=events)
#restful routes 
""" there are 7 restful routes but, in the main, 5. 2 double up
"""
@app.route('/events', methods=["POST"])
def add_event():
    event_date = request.form['date']
    event_name = request.form['name']
    event_number_of_guests = request.form['guests']
    event_room_location = request.form['room']
    event_description = request.form['description']
    new_event = Event(event_date, event_name, event_number_of_guests, event_room_location, event_description, False)
    events.append(new_event)

    return render_template("index.html", title="Events", all_events=events)
