from .error_types.http_conflict import HttpConflict
from .error_types.http_not_found import HttpNotFound
from src.http_types.http_response import HttpResponse

def handler_errors(error: Exception) -> HttpResponse:
    if isinstance(error, (HttpConflict, HttpNotFound)):
        return HttpResponse(
            body= {
                'errors': [
                    {
                        'title': error.name,
                        'details': error.message,
                        
                    }
                ]
            },
            status_code= error.status_code
        )
    return HttpResponse(
        body= {
            'errors':[{
                'title': 'error',
                'details': str(error)
            }]
        },
        status_code=500
    )