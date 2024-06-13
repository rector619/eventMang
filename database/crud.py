import uuid
import copy
from cassandra.cqlengine.management import sync_table

from .db import get_session
from routers.events.models import Event, EventScrapeEvent, EventScrapeModel

session = get_session()
sync_table(Event)
sync_table(EventScrapeModel)
sync_table(EventScrapeEvent)

#user creates event on plaform
def create_entry(data:dict):
    data['event_id'] = uuid.uuid1() #includes a timestamp
    return Event.create(**data)

#create event scareped
def create_scrape_model_entry(data:dict):
    return EventScrapeModel.create(**data)

def create_scrape_entry(data:dict):
    data['uuid'] = uuid.uuid1() #includes a timestamp
    return EventScrapeEvent.create(**data)

def add_scrape_entry(data:dict, fresh: False):
    if fresh:
        data = copy.deepcopy(data)
    product = create_entry(data)
    scrape_obj = create_scrape_entry(data)
    return product, scrape_obj


#moved to main
def update_entry(data:dict):
    Event.filter()
    return Event.update()
