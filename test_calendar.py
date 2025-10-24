from my_calendar import get_events

def test_events_are_in_list():
    events = get_events()
    assert isinstance(events, list)