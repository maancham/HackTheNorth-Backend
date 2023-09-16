from decouple import config
from storages.backends.s3boto3 import S3Boto3Storage

from link_chaincloak_django.settings.components.common import DEBUG
from link_chaincloak_django.storage_backends.custom_file_storage import CustomFileStorage

BASE_MEDIA_LOCATION = "media"


class S3MediaStorage(S3Boto3Storage):
    location = "media"
    file_overwrite = True


if not DEBUG or not config("STAGING", default=True):
    MediaStorage = S3MediaStorage
else:
    MediaStorage = CustomFileStorage
