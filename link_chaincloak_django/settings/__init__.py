from .components.applications import *
from .components.auth import *
from .components.aws import *
from .components.caches import *

from .components.common import *
from .components.constants import *
from .components.database import *
from .components.django import *
from .components.django_headers_config import *
from .components.internationalization import *

from .components.locale import *

from .components.messages import *
from .components.middleware import *
from .components.rest_framework import *
from .components.sentry import *
from .components.server_address import get_server_add
from .components.storages import *
from .components.templates import *

PROJECT_NAME = os.getenv("APP_BASE_NAME")  # noqa: F405
