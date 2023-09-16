import logging

from rest_framework import serializers
from rest_framework.serializers import ValidationError

from apps.shared.exceptions import CustomValidationError
from utils.general.logger import Logger

logger = logging.getLogger("custom")


class HiddenErrorModelSerializer(serializers.Serializer):
    def is_valid(self, *, raise_exception=False):
        try:
            return super().is_valid(raise_exception=raise_exception)
        except ValidationError as exc:
            request = self.context["request"]
            user = str(request.user.id) if request and request.user and request.user.is_authenticated else "anonymous"
            Logger().error(
                logger,
                title="serializer validation error",
                message=str(exc),
                additional_data={"url": request.path if request else None, "user": user},
            )
            raise CustomValidationError()
