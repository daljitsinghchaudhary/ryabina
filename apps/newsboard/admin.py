# coding=utf-8
from django.contrib import admin
from tinymce.widgets import TinyMCE
from apps.newsboard.models import News


class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'is_published', 'on_main_page',)
    list_display_links = ('title',)
    list_filter = ('is_published',)
    search_fields = ('title', 'announce', 'content')
    date_hierarchy = 'created_at'
    fieldsets = (
        (None, {
            'fields': ('title', 'created_at', 'on_main_page', 'is_published', 'image', 'announce', 'content', 'close_at')
        }),
    )

admin.site.register(News, NewsAdmin)
