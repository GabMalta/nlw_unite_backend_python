from typing import Dict
from src.models.settings.connection import db_connect
from src.models.entities.events import Events

class EventsRepository:
    def insert_event(self, eventsInfo:Dict) -> Dict:
        with db_connect as db:
            event = Events(
                id = eventsInfo.get('uuid'),
                title = eventsInfo.get('title'),
                details = eventsInfo.get('details'),
                slug = eventsInfo.get('slug'),
                maximum_attendees = eventsInfo.get('maximum_attendees')
            )
            
            db.session.add(event)
            db.session.commit()
            
            return eventsInfo
    
    def get_event_by_id(self, event_id : str) -> Events:
        with db_connect as db:
            event = (
                db.session
                    .query(Events)
                    .filter(Events.id == event_id)
                    .one()
            )
            
            return event