import uuid
from src.models.entities.check_ins import CheckIns
from src.models.repository.check_ins_repository import CheckInRepository
from src.http_types.http_response import HttpResponse
from src.http_types.http_request import HttpRequest


class CheckInHandler:
    def __init__(self):
        self.__check_in_repository = CheckInRepository()
        
    def register(self, http_request : HttpRequest) -> HttpResponse:
        check_in_infos = http_request.param['attendee_id']
        self.__check_in_repository.insert_check_in(check_in_infos)
        
        return HttpResponse(
            body=None,
            status_code= 201
        )