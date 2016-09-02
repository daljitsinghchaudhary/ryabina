# coding=utf8
from django.contrib import admin
from tinymce.widgets import TinyMCE
from apps.discounts.models import Discount


class DiscountServicesInline(admin.TabularInline):
     model = Discount.services.through
     raw_id_fields = ('service',)
     extra = 1


class DiscountAdmin(admin.ModelAdmin):
    list_display = ('title', 'image', 'current_price', 'old_price', 'percent', 'close_at', 'created_at', 'is_published')
    list_display_links = ('title',)
    date_hierarchy = 'created_at'
    search_fields = ('title',)
    list_filter = ('is_published',)
    fieldsets = (
        (None, {
            'fields': ('title', 'image', 'content', 'url', 'button', 'current_price', 'old_price', 'percent', 'close_at', 'created_at', 'is_published'),
        }),
    )
    inlines = (DiscountServicesInline,)
    exclude = ('services',)


admin.site.register(Discount, DiscountAdmin)