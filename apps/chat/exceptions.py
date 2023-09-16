from rest_framework.exceptions import APIException


class InvalidRequestError(APIException):
    def __init__(self, detail="invalid request error"):
        self.default_code = "invalid_request_error"
        super().__init__(detail, self.default_code)
        self.default_detail = detail


class ServiceCallError(APIException):
    def __init__(self, detail="service call error"):
        self.default_code = "service_call_error"
        super().__init__(detail, self.default_code)
        self.default_detail = detail
