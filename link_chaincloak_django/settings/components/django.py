import os

from django.conf import settings

from .common import BASE_DIR, DEBUG
from .constants import PROJECT_NAME

SECRET_KEY = os.getenv("SECRET_KEY", "6324$#@$FDSzdfe9kjkhj&w=k@j5msdfrr4@cq*adsf@ag6asdci3cng&6")

ALLOWED_HOSTS = ["*"]

if DEBUG:
    ALLOWED_HOSTS += ["127.0.0.1", "localhost", "*"]

INTERNAL_IPS = ["127.0.0.1"]

ROOT_URLCONF = f"{PROJECT_NAME}.urls"

MEDIA_URL = "/medias/"
MEDIA_ROOT = os.path.join(BASE_DIR, "medias")

WSGI_APPLICATION = f"{PROJECT_NAME}.wsgi.application"

# Configure HTTPS
USE_X_FORWARDED_HOST = True

SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

if not settings.DEBUG:
    SECURE_CONTENT_TYPE_NOSNIFF = True
    SECURE_CROSS_ORIGIN_OPENER_POLICY = "same-origin"
    SECURE_HSTS_INCLUDE_SUBDOMAINS = True
    SECURE_HSTS_PRELOAD = True
    SECURE_HSTS_SECONDS = 86400
    SECURE_REDIRECT_EXEMPT = []
    SECURE_REFERRER_POLICY = "same-origin"
    CSRF_TRUSTED_ORIGINS = [
        "http://localhost:8000",
        "http://localhost:3000",
    ]
