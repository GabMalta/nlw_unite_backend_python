from flask import Blueprint, jsonify, request
from src.http_types.http_request import HttpRequest
from src.data.check_in_handler import CheckInHandler
from src.errors.errors_handler import handler_errors

check_in_route_bp = Blueprint('check_in_route', __name__)

@check_in_route_bp.route('/attendees/<attendee_id>/check-in', methods=['POST'])
def create_check_in(attendee_id):
    try:
        http_request = HttpRequest(param={'attendee_id': attendee_id})
        check_in_handler = CheckInHandler()
        
        http_response = check_in_handler.register(http_request)
    
    except Exception as exception:
        http_response = handler_errors(exception)
    
    return jsonify(http_response.body), http_response.status_code