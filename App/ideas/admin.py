from django.contrib import admin
from django.utils.html import format_html

from .models import Idea, Vote


class VoteInLine(admin.StackedInline):
    model = Vote


@admin.register(Idea)
class IdeaAdmin(admin.ModelAdmin):
    search_fields = ['title']
    list_display = ['title', 'status', 'show_app_url']
    list_filter = ['status']
    inlines = [
        VoteInLine
    ]

    def show_app_url(self, obj):
        if obj.app_url is not None:
            return format_html(f'<a href="{obj.app_url}" target="_blanc">"{obj.app_url}"</a>')
        else:
            return ''

    show_app_url.short_description = "APP URL"


@admin.register(Vote)
class VoteAdmin(admin.ModelAdmin):
    list_display = ['id', 'idea', 'reason']
    list_filter = ['idea']
