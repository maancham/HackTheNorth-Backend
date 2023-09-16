from django.urls import include, path

local_apps_urlpatterns = [
    path("chat/", include(("apps.chat.urls", "apps.chat"), namespace="v1")),
    path("users/", include(("apps.users.urls", "apps.users"), namespace="v1")),
]
