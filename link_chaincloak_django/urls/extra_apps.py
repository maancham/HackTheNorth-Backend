from django.conf import settings
from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

extra_apps_urlpatterns = [
    path("ht/", include("health_check.urls")),
]

if settings.DEBUG:
    extra_apps_urlpatterns += [
        path("schema/", SpectacularAPIView.as_view(api_version="v1"), name="schema"),
        path(
            "docs/",
            SpectacularSwaggerView.as_view(template_name="swagger-ui.html", url_name="schema"),
            name="swagger-ui",
        ),
    ]
