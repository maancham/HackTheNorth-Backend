from django.contrib import admin
from django.urls import path

from link_chaincloak_django.settings import PROJECT_NAME

admin.site.site_title = PROJECT_NAME
admin.site.index_title = f"{PROJECT_NAME} Platform"
admin.site.site_header = f"{PROJECT_NAME}"

admin_urlpatterns = [
    path("admin/", admin.site.urls, name="admin"),
]
