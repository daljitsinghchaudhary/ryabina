# coding=utf-8
from django.contrib import admin
from models import StaticText

class StaticTextAdmin(admin.ModelAdmin):
    list_display = (u'key', u'text', u'sites_changelist')

admin.site.register(StaticText, StaticTextAdmin)