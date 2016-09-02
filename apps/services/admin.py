# coding=utf8
from django.contrib import admin
from models import ServiceIcon, Service, ServiceCourse, ServiceCategory
from treebeard.admin import TreeAdmin
from treebeard.forms import movenodeform_factory


class ServiceAdmin(TreeAdmin):
    form = movenodeform_factory(Service)
    list_display = ('title', 'course', 'get_categories_changelist', 'get_price_changelist')
    list_filter = ('course', 'category')
    search_fields = ('title',)
    fields = ('title', 'min_price', 'max_price', '_position', '_ref_node_id', 'course', 'category')


class ServiceCategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'get_services_count')
    search_fields = ('title',)


class ServiceCourseAdmin(admin.ModelAdmin):
    list_display = ('title',)


admin.site.register(ServiceIcon)
admin.site.register(ServiceCategory, ServiceCategoryAdmin)
admin.site.register(ServiceCourse, ServiceCourseAdmin)
admin.site.register(Service, ServiceAdmin)