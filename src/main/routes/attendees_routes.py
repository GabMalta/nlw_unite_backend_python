from flask import Blueprint, jsonify, request
from src.http_types.http_request import HttpRequest
from src.data.attendees_handler import AttendeesHandler
from src.errors.errors_handler import handler_errors

attendee_route_bp = Blueprint('attendee_route', __name__)

@attendee_route_bp.route('/events/<event_id>/register', methods=['POST'])
def create_attendee(event_id):
    try:
        http_request = HttpRequest(body=request.json, param={'event_id': event_id})
        attendee_handler = AttendeesHandler()
        
        http_response = attendee_handler.register(http_request)
    except Exception as exception:
        http_response = handler_errors(exception)
    
    return jsonify(http_response.body), http_response.status_code

@attendee_route_bp.route('/attendees/<attendee_id>/badge', methods=['GET'])
def find_badge_attendee(attendee_id):
    try:
        http_request = HttpRequest(param={'attendee_id': attendee_id})
        attendee_handler = AttendeesHandler()
        http_response = attendee_handler.find_attendee_badge(http_request)
    
    except Exception as exception:
        http_response = handler_errors(exception)
    
    return jsonify(http_response.body), http_response.status_code

@attendee_route_bp.route('/events/<event_id>/attendees', methods=['GET'])
def get_attendees(event_id):
    try:
        http_request = HttpRequest(param={'event_id': event_id})
        attendee_handler = AttendeesHandler()
        http_response = attendee_handler.find_attendees_from_event_id(http_request)
    
    except Exception as exception:
        http_response = handler_errors(exception)
    
    return jsonify(http_response.body), http_response.status_code