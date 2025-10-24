from my_calendar import get_events, create_events, get_list_events, get_chronologic_events
from datetime import datetime

def test_events_are_in_list():
    events = get_events()
    assert isinstance(events, list)

def test_create_events():
    T = "2024-01-01 10:00:00"
    t = 3600
    n = "Réunion"
    event = create_events(T,t,n)
    assert isinstance(event,tuple)
    assert len(event) == 3
    assert isinstance(event[0],str)
    assert isinstance(event[1],int)
    assert isinstance(event[2],str)

def test_get_list_events():
    list_of_events = get_list_events()
    assert isinstance(list_of_events, list)
    for event in list_of_events:
        assert isinstance(event, tuple)
        assert len(event) == 3
        assert isinstance(event[0],str)
        assert isinstance(event[1],int)
        assert isinstance(event[2],str)

def test_get_chronologic_event():
        event1 = create_events(datetime(2024,1,3,10,0,0),3600,"Event 1")
        event2 = create_events(datetime(2024,1,1,9,0,0),1800, "Event 2")
        chronologic_list_events = get_chronologic_events()
        assert  chronologic_list_events[0] == event2
        assert chronologic_list_events[1] == event1
