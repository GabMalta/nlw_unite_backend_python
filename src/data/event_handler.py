import uuid
from src.models.repository.events_repository import EventsRepository
from src.http_types.http_response import HttpResponse
from src.http_types.http_request import HttpRequest
from src.models.entities.events import Events

class EventHandler:
    def __init__(self):
        self.__envents_repository = EventsRepository()
        
    def register(self, http_request: HttpRequest) -> HttpResponse:
        body = http_request.body
        body['uuid'] = str(uuid.uuid4())
        self.__envents_repository.insert_event(body)
        
        return HttpResponse(
            body={'eventId': body['uuid']},
            status_code= 200
        )
        
    def get_event(self, http_request: HttpRequest) -> HttpResponse:
        event_id = http_request.param['event_id']
        event = self.__envents_repository.get_event_by_id(event_id)
        event_attendees_count = self.__envents_repository.count_event_attendees(event_id)
        
        if not event: raise Exception("Evento não encontrado")
        
        return HttpResponse(
            body={
                'event': {
                    'id': event.id,
                    'title': event.title,
                    'details': event.details,
                    'slug': event.slug,
                    'maximumAttendees': event.maximum_attendees,
                    'attendeesAmount': event_attendees_count['amountAttendees']
                }
            },
            status_code= 200
        )