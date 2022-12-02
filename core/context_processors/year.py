from datetime import datetime
from django.http import HttpRequest, HttpResponse


def year(request: HttpRequest) -> HttpResponse:
    """Add info about year."""
    year = datetime.strftime(datetime.now(), "%Y")
    result = {"year": year}
    return result
