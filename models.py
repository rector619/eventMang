# from email.policy import default
# from cassandra.cqlengine import columns
# from cassandra.cqlengine.models import Model

# data = {
#     "eventbrite_event_id":"12343423233",
#     "name": "Retro Party"
# }

# my_events = {
#     "event_name": "title of post 1", 
#     "organizer":"content of event 1",
#     "type":"house party",
#     "category":"ight",
#     "price_str":"100"
#     }

# #List View -> Detail View
# #scraped events
# class EventScrapeModel(Model): #-> table
#     __keyspace__ = "api_scrapper_app1"
#     eventbrite_event_id = columns.Text(primary_key = True, required=True)
#     name = columns.Text()
#     price_str=columns.Text(default="-100")

# #Detail view for eventbrite_event_id
# class EventScrapeEvent(Model): #-> table
#     __keyspace__ = "api_scrapper_app1"
#     uuid = columns.UUID(primary_key = True )
#     eventbrite_event_id = columns.Text(index=True)
#     name = columns.Text()
#     price_str=columns.Text(default="-100")

# #user creates event on plaform
# class Event(Model):
#     __keyspace__ = "api_scrapper_app1"
#     event_id = columns.UUID(primary_key = True)
#     event_name = columns.Text()
#     organizer = columns.Text()
#     type = columns.Text()
#     category =columns.Text()
#     price_str=columns.Text(default="-100")

# class Type(Model):
#      __keyspace__ = "api_scrapper_app1"
#      id = columns.UUID(primary_key=True)
#      type_name = columns.Text()
