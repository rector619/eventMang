from fastapi import APIRouter, status, HTTPException
from . import models 
from routers.events.models import EventSattic
from uuid import UUID
from database import crud

router = APIRouter(
    prefix='/events',
    tags=['events']
)

Event = models.Event
EventScrapeEvent = models.EventScrapeEvent


my_events = [{"id":1, "event_name": "title of post 1", "content":"content of event 1"},
             {"id":2, "event_name": "African Leaders", "content":"content of event 2" }]



def find_event(id):
    for e in my_events:
        if e['id'] == id:
            return e


@router.get("/cqlevents")
def test_post():
    events = list(Event.all())
    # return events
    return {'data': events}

@router.get("/events")
def get_events():
    events = list(Event.all())
    # my_events = EventSattic.objects
    return {"data": events}


@router.post("/events", status_code=status.HTTP_201_CREATED)
def create_events(event: EventSattic):
    new_event = crud.create_entry(event)
    return {"message": new_event}
#event title, organizer, type, category


 #get event by id in CQL
@router.get("/events/{id}")
def get_event(id: UUID):
    event =  list(Event.filter(Event.event_id == id))
    print(event)
    if not event:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id: {id} was not found")
        
    return {"event_detail":event}

 
 #update event in CQL
@router.put("/events/{id}")
def update_event(id: UUID, event: EventSattic):
    event_query = Event.filter(Event.event_id == id)
    event = event_query
    print('event',event)
    event.update()
    if event.if_not_exists():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id: {id} does not exist")

    
    return {"date": "success"}
