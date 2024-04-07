from flask import Blueprint, jsonify, request
from src.http_types.http_request import HttpRequest
from src.data.attendees_handler import AttendeesHandler

attendee_route_bp = Blueprint('attendee_route', __name__)

@attendee_route_bp.route('/events/<event_id>/register', methods=['POST'])
def create_attendee(event_id):
    http_request = HttpRequest(body=request.json, param={'event_id': event_id})
    attendee_handler = AttendeesHandler()
    
    http_response = attendee_handler.register(http_request)
    
    return jsonify(http_response.body), http_response.status_code

@attendee_route_bp.route('/attendees/<attendee_id>/badge', methods=['GET'])
def find_badge_attendee(attendee_id):
    http_request = HttpRequest(param={'attendee_id': attendee_id})
    attendee_handler = AttendeesHandler()
    print(f'2--> {http_request}')
    http_response = attendee_handler.find_attendee_badge(http_request)
    
    return jsonify(http_response.body), http_response.status_code