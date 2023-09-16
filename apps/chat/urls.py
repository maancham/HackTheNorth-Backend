from django.urls import path

from apps.chat.apis.chat import ChatApi

urlpatterns = [
    path("chat/<str:service>", ChatApi.as_view(), name="chat"),
]
