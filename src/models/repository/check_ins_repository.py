from src.models.settings.connection import db_connect
from src.models.entities.check_ins import CheckIns
from sqlalchemy.exc import IntegrityError, NoResultFound
from src.errors.error_types.http_conflict import HttpConflict

class CheckInRepository:
    def insert_check_in(self, attendee_id):
        try:
            with db_connect as db:
                check_in = CheckIns(attendeeId = attendee_id)
                db.session.add(check_in)
                db.session.commit()
                
                return attendee_id
                
        except IntegrityError:
                raise HttpConflict('Check-in já efetuado!')
            
        except Exception as exception:
                db.session.rollback()
                raise exception
        