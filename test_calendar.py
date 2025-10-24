from my_calendar import get_events, create_events

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

