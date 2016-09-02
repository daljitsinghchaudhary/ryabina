# -*- coding: utf-8 -*-

from django.contrib import admin
from django import forms
from tinymce.widgets import TinyMCE
from apps.pages.models import FlatPage, FlatPageDoc


class FlatPageDocInline(admin.StackedInline):
    model = FlatPageDoc
    sortable_field_name = 'order'
    extra = 0

    def formfield_for_dbfield(self, db_field, **kwargs):
        if db_field.name == 'order':
            kwargs['widget'] = forms.widgets.HiddenInput()
        return super(FlatPageDocInline, self).formfield_for_dbfield(db_field, **kwargs)


class FlatPageAdminForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(FlatPageAdminForm, self).__init__(*args, **kwargs)
        self.fields['parent'].queryset = FlatPage.objects.exclude(id__exact=self.instance.pk).filter(parent__isnull=True)


class FlatPageAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_select_related = True
    list_display = ('title_with_margin', 'url', 'is_published',)
    form = FlatPageAdminForm
    fieldsets = (
        (None, {
            'fields': ('title', 'slug', 'is_published', 'parent', 'content',)
        }),
        (u'Метатеги', {
            'classes': ('collapse closed',),
            'fields': ('meta_title', 'meta_keywords', 'meta_description',)
        }),
    )
    inlines = [FlatPageDocInline]

    def title_with_margin(self, obj):
        if obj.parent:
                return u'---- %s' % obj.title
        return u'%s' % obj.title
    title_with_margin.short_description = u'Заголовок'

    def formfield_for_dbfield(self, db_field, **kwargs):
        if db_field.name == 'content':
            kwargs['widget'] = TinyMCE(attrs={'cols': 100, 'rows': 40},)
        return super(FlatPageAdmin, self).formfield_for_dbfield(db_field, **kwargs)

admin.site.register(FlatPage, FlatPageAdmin)