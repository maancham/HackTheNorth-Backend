from drf_spectacular.utils import extend_schema_view, extend_schema
from rest_framework import serializers
from rest_framework.views import APIView

from apps.chat.exceptions import InvalidRequestError
from apps.chat.services.cohere_service import CohereService
from apps.chat.services.open_ai_service import OpenAIService
from apps.shared.response import SuccessResponse


class MessageSerializer(serializers.Serializer):
    content = serializers.CharField(required=True)
    role = serializers.CharField(required=True)


class ChatRequestSerializer(serializers.Serializer):
    messages = MessageSerializer(many=True, required=True)


@extend_schema_view(post=extend_schema(request=ChatRequestSerializer))
class ChatApi(APIView):
    services = {"openai": OpenAIService, "cohere": CohereService}

    def post(self, request, service, *args, **kwargs):
        service = self.services.get(service, OpenAIService)()
        if "messages" not in request.data:
            raise InvalidRequestError()
        result = service.chat(request.data["messages"])
        return SuccessResponse(result)
