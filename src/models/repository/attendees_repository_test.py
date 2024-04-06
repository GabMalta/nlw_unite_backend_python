import pytest
from .attendees_repository import AttendeesRepository
from src.models.settings.connection import db_connect

db_connect.connect_to_db()

def test_insert_attendee():
    attendee_info = {
        'uuid' : 'meu-attendee-uuid',
        'name' : 'meu-attendee-name',
        'email' : 'meu-attendee-email',
        'event_id' : 'uuid-ttteste',
    }
    
    attendee_repository = AttendeesRepository()
    response = attendee_repository.insert_attendee(attendee_info)
    
    print(response)
    