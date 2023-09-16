from storages.backends.s3boto3 import S3Boto3Storage


class StaticStorage(S3Boto3Storage):
    BASE_LOCATION = "static"
    location = "static"
