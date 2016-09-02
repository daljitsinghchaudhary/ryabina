# coding=utf8
from django.contrib import admin
from models import RotatingImage, ParallaxImage, ContactsImage, ContactsImagesType


class RotatingImageAdmin(admin.ModelAdmin):
    list_display = ('title', 'image', 'content', 'url', 'button')
    list_display_links = ('title',)
    search_fields = ('title',)
    fieldsets = (
        (None, {
            'fields': list_display,
        }),
    )


admin.site.register(ContactsImage)
admin.site.register(ContactsImagesType)
admin.site.register(ParallaxImage)
admin.site.register(RotatingImage, RotatingImageAdmin)