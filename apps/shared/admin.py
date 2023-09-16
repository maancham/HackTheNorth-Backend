from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html
from django_admin_inline_paginator.admin import TabularInlinePaginated
from django_autoutils.admin_utils import (
    AvatarAdmin,
    EditLinkAdmin,
)
from django_object_actions import DjangoObjectActions


class BaseAdmin:
    exclude = ("creator",)


class CacheAwareModelAdmin:
    """
    Handle cache data
    """

    def save_model(self, request, obj, form, change: bool):
        # noinspection PyUnresolvedReferences
        if "creator" in [f.name for f in obj._meta.fields]:
            if not obj.creator:
                obj.creator = request.user
        super().save_model(request, obj, form, change)
        self.invalidate_cache(obj, change)

    def invalidate_cache(self, obj, change):
        pass


class BaseModelAdmin(
    DjangoObjectActions,
    AvatarAdmin,
    CacheAwareModelAdmin,
    BaseAdmin,
    admin.ModelAdmin,
):
    """
    Base admin for all models
    """

    readonly_fields = (
        "created_date",
        "modified_date",
        "creator",
    )

    def get_obj(self, obj):
        """
        Get not person object
        """
        if not obj:
            return None
        return self._get_obj(obj)

    # noinspection PyMethodMayBeStatic
    def _get_obj(self, obj):
        if hasattr(obj, "get_obj"):
            return obj.get_obj()
        return obj

    def _get_avatar_obj(self, obj):
        return self.get_obj(obj)


class BaseTabularInlineAdmin(AvatarAdmin, EditLinkAdmin, BaseAdmin, TabularInlinePaginated):
    """
    Base admin for all inlines
    """

    pass


class BaseStackedInlineAdmin(BaseTabularInlineAdmin):
    """
    Base admin for all inlines
    """

    template = "admin/edit_inline/stacked.html"


def linkify(field_name):
    """
    Converts a foreign key value into clickable links.

    If field_name is 'parent', link text will be str(obj.parent)
    Link will be admin url for the admin url for obj.parent.id:change
    """

    def _linkify(obj):
        linked_obj = getattr(obj, field_name)
        if linked_obj is None:
            return "-"
        app_label = linked_obj._meta.app_label
        model_name = linked_obj._meta.model_name
        view_name = f"admin:{app_label}_{model_name}_change"
        link_url = reverse(view_name, args=[linked_obj.pk])
        return format_html('<a href="{}">{}</a>', link_url, linked_obj)

    _linkify.short_description = field_name  # Sets column name
    return _linkify
