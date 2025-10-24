events_storage=[]
def get_events():
    return []

def create_events(T,t,n):
    event= (T,t,n)
    events_storage.append(event)
    return event

def get_list_events():
    return events_storage

def get_chronologic_events():
        events = get_list_events()
        sorted_events = sorted(events, key=lambda event: event[0])
        return sorted_events


def get_first_event():
    events_storage = get_list_events()
    return events_storage[0]