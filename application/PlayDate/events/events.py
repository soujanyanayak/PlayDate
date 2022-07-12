from django.db.models import Q
from events.models import  Publicevent, Address, Event

# DB table event missing event_name, date_time, event_description, interests
# input location details need to be split into street, city, state, country, zipcode
# assuming location as dictionary
def createEvent(event_name, date_time, location):

    
