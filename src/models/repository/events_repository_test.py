import pytest
from .events_repository import EventsRepository
from src.models.settings.connection import db_connect

db_connect.connect_to_db()

@pytest.mark.skip(reason='Novo Registro em Banco de Dados')
def test_insert_events():
    
    event = {
        'uuid': 'uuid-ttteste',
        'title': 'meu-title',
        'details': 'meu-detail',
        'slug': 'meu-slug',
        'maximum_attendees': 20
    }
    
    events_repository = EventsRepository()
    response = events_repository.insert_event(event)
    
    print(response)
    
#@pytest.mark.skip(reason='Novo Registro em Banco de Dados')    
def test_get_event_by_id():
    event_id = 'uuid-ttteste22'
    events_repository = EventsRepository()
    response = events_repository.get_event_by_id(event_id)
    
    print(response)