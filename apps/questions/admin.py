# coding=utf-8
from django.contrib import admin
from apps.questions.models import Callback, EmailRecipient, Visit, Question, VisitPurpose


class EmailRecipientAdmin(admin.ModelAdmin):
    list_display = ('recipient_email', 'email_type_changelist')


class CallbackAdmin(admin.ModelAdmin):
    list_display = ('created_at', 'name', 'phone', 'get_callback_delta_changelist', 'callback_time', 'processed_at')

    fieldsets = (
        (None, {
            'fields': ('created_at', 'name', 'phone', 'callback_delta', 'callback_time', 'processed_at')
        }),
    )

    readonly_fields = ('created_at', 'callback_time')


class VisitAdmin(admin.ModelAdmin):
    list_display = ('created_at', 'name', 'phone', 'get_procedure_changelist', 'purpose', 'visit_date', 'visit_time')

    fieldsets = (
        (None, {
            'fields': ('created_at', 'name', 'phone', 'procedure', 'purpose', 'visit_date', 'visit_time', 'description', 'processed_at')
        }),
    )

    readonly_fields = ('created_at', )


admin.site.register(Callback, CallbackAdmin)
admin.site.register(EmailRecipient, EmailRecipientAdmin)
admin.site.register(Visit, VisitAdmin)
admin.site.register(Question)
admin.site.register(VisitPurpose)
