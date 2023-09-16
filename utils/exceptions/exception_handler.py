from rest_framework.views import exception_handler
from rest_framework.exceptions import ValidationError
from django.utils.translation import gettext as _
from django.http.response import Http404


def custom_exception_handler(exc, context):
    response = exception_handler(exc, context)

    if response is not None:
        if isinstance(exc, ValidationError):
            exc.default_code = "invalid_input"
            exc.default_detail = _("Some field is required.")
        if isinstance(exc, Http404):
            exc.default_code = "no_match_found"
            exc.default_detail = _("No match found.")
        response.data = _handel_generic_error(exc)
    return response


def _handel_generic_error(exc):
    try:
        version = exc.version
    except Exception:  # noqa: E722
        version = "v1"
    code = getattr(exc, "default_code", None)
    try:
        get_codes = getattr(exc, "get_codes", None)
        code = get_codes()
    except Exception:
        pass
    return {
        "error": {
            "code": code,
            "detail": getattr(exc, "detail", None),
            "version": version,
        }
    }
