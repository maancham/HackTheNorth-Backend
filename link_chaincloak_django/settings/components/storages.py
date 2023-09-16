import os

from .common import BASE_DIR, DEBUG
from .constants import PROJECT_NAME

STATIC_URL = os.getenv("STATIC_URL", "/static/")
STATIC_ROOT = os.path.join(BASE_DIR, "static")
STATICFILES_DIRS = [os.path.join(BASE_DIR, "templates/admin/static")]
if not DEBUG or os.getenv("STAGING", False):
    STATICFILES_STORAGE = f"{PROJECT_NAME}.storage_backends.StaticStorage"

# Media
MEDIA_URL = os.getenv("MEDIA_URL", "/media/")
MEDIA_ROOT = os.path.join(BASE_DIR, "media")
if not DEBUG or os.getenv("STAGING", False):
    PUBLIC_MEDIA_LOCATION = "media"
    DEFAULT_FILE_STORAGE = f"{PROJECT_NAME}.storage_backends.MediaStorage"
