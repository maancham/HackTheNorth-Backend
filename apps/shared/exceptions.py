from django.utils.translation import gettext_lazy as _
from rest_framework.exceptions import APIException


class IncompleteRequestException(APIException):
    status_code = 400
    default_detail = _("incomplete request")
    default_code = "incomplete_request"


class InvalidRequestException(APIException):
    status_code = 400
    default_detail = _("invalid request")
    default_code = "invalid_request"


class CustomException(APIException):
    def __init__(self, status_code, message, code):
        self.status_code = status_code
        self.detail = message
        self.default_detail = message
        self.default_code = code if code else message.replace(" ", "_")


class CustomValidationError(APIException):
    status_code = 400

    def __init__(self, detail=_("validation error")):
        self.default_code = "validation_error"
        super().__init__(detail, self.default_code)
        self.default_detail = detail


class OpenStreetCallError(APIException):
    status_code = 417

    def __init__(self, detail=_("Failed to call open street service")):
        self.default_code = "open_street_error"
        super().__init__(detail, self.default_code)
        self.default_detail = detail
