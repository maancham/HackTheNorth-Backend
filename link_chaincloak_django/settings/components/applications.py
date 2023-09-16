# Application definition
LOCAL_APPS = [
    "apps.users",
    "apps.chat",
]

THIRD_PARTY_APPS = [
    "rest_framework",
    "rest_framework.authtoken",
    "django_extensions",
    "debug_toolbar",
    "storages",
    "corsheaders",
    "multiselectfield",
    "simple_history",
    "health_check",
    "health_check.db",
    "health_check.storage",
    "admin_auto_filters",
    "drf_spectacular",
    "django_object_actions",
]

DEFAULT_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]

LATE_LOAD_THIRD_PARTY_APPS = []

INSTALLED_APPS = DEFAULT_APPS + THIRD_PARTY_APPS + LOCAL_APPS + LATE_LOAD_THIRD_PARTY_APPS
