from typing import Dict
from src.models.settings.connection import db_connect
from src.models.entities.events import Events
from src.models.entities.attendees import Attendees
from sqlalchemy.exc import IntegrityError, NoResultFound

class EventsRepository:
    def insert_event(self, eventsInfo:Dict) -> Dict:
        with db_connect as db:
            try:
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
            
            except IntegrityError:
                raise Exception('Evento já cadastrado!')

            except Exception as exception:
                db.session.rollback()
                raise exception
    
    def get_event_by_id(self, event_id : str) -> Events:
        with db_connect as db:
            try:
                event = (
                    db.session
                        .query(Events)
                        .filter(Events.id == event_id)
                        .one()
                )
                
                return event
            
            except NoResultFound:
                return None
    
    def count_event_attendees(self, event_id : str) -> Dict:
        with db_connect as db:
            try:
                event_count = (
                    db.session
                        .query(Events)
                        .join(Attendees, Attendees.event_id == event_id)
                        .filter(Events.id == event_id)
                        .all()
                )
                
                if not len(event_count):
                    return {
                        'maximumAttendees': 0,
                        'amountAttendees': 0
                    }
                    
                return {
                    'maximumAttendees': event_count[0].maximum_attendees,
                    'amountAttendees': len(event_count)
                }
                
            except NoResultFound:
                return None
            
            except Exception as exception:
                db.session.rollback()
                raise exception