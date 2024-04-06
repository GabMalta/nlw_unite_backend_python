from src.models.settings.base import Base
from sqlalchemy import column, String, Integer

class Attendees(Base):
    id = column(String, primary_key=True)
    name = column(String, nullable=False)
    email = column(String, nullable=False)
    event_id = column(String, nullable=False)
    
    
    # "id" TEXT NOT NULL PRIMARY KEY,
    # "name" TEXT NOT NULL,
    # "email" TEXT NOT NULL,
    # "event_id" TEXT NOT NULL,
    # "created_at" DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    # CONSTRAINT "attendees_event_id_fkey" FOREIGN KEY ("event_id") REFERENCES "events" ("id") ON DELETE RESTRICT ON UPDATE CASCADE