from uuid import UUID

from fastapi import Body, FastAPI, Response, status, HTTPException

from random import randrange
import config
from database import crud, db
from routers.events import models
from cassandra.cqlengine.management import sync_table, drop_table
from routers.users.models import User
from routers.vendors.models import VendorOrBusiness
from routers.users import user
from routers.events import event
from routers.vendors import vendor


Event = models.Event
EventScrapeEvent = models.EventScrapeEvent


settings = config.get_settings()

app = FastAPI()

app.include_router(user.router)
app.include_router(event.router)
app.include_router(vendor.router)
session = None

@app.get("/")
def read_index():
    return {"welcome": "to my event", "keyspace": settings.keyspace, "db_client_id":settings.db_client_id}


@app.on_event("startup")
def on_startup():
    global session 
    session = db.get_session()
    # drop_table(VendorOrBusiness)
    sync_table(User)
    sync_table(Event)
    sync_table(EventScrapeEvent)
    sync_table(VendorOrBusiness)
    




# class EventSattic(BaseModel):
#     # event_id: UUID
#     event_name: str
#     organizer: str 
#     type: str
#     category: str
#     price_str: str
#     tags: Optional[str] = None

  

# my_events = [{"id":1, "event_name": "title of post 1", "content":"content of event 1"},
#              {"id":2, "event_name": "African Leaders", "content":"content of event 2" }]



# def find_event(id):
#     for e in my_events:
#         if e['id'] == id:
#             return e


# @app.get("/cqlevents")
# def test_post():
#     events = list(Event.all())
#     # return events
#     return {'data': events}

# @app.get("/events")
# def get_events():
#     events = list(Event.all())
#     # my_events = EventSattic.objects
#     return {"data": events}


# @app.post("/events", status_code=status.HTTP_201_CREATED)
# def create_events(event: EventSattic):
#     new_event = crud.create_entry(event)
#     return {"message": new_event}
# #event title, organizer, type, category


#  #get event by id in CQL
# @app.get("/events/{id}")
# def get_event(id: UUID):
#     event =  list(Event.filter(Event.event_id == id))
#     print(event)
#     if not event:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id: {id} was not found")
        
#     return {"event_detail":event}

 
#  #update event in CQL
# @app.put("/events/{id}")
# def update_event(id: UUID, event: EventSattic):
#     event_query = Event.filter(Event.event_id == id)
#     event = event_query
#     print('event',event)
#     event.update()
#     if event.if_not_exists():
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id: {id} does not exist")

    
#     return {"date": "success"}


# @app.post("/events", status_code=status.HTTP_201_CREATED)
# def create_events(event: EventSattic):
#     event_dict = event.dict()
#     event_dict['id'] = randrange(0, 100000)
#     my_events.append(event_dict)
#     return {"message":event_dict}

# @app.get("/events/{id}")
# def get_event(id: int, response: Response):
#     event = find_event(id)
#     if not event:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id: {id} was not found")
        
#     return {"event_detail":event}


