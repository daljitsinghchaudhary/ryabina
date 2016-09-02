# coding=utf-8
import datetime
from django.conf import settings
from django.contrib.sites.models import Site
from django.core.mail import send_mail
from django.db import models
from django.db.models.signals import post_save
from django.template import Context
from django.template.loader import get_template
from django.utils import timezone
from request_provider.signals import get_request

if settings.DEBUG:
    import logging
    signals_logger = logging.getLogger('signals')


class EmailTypesEnum(object):
    FEEDBACK = 0
    CALLBACK = 1
    VISIT = 2
    QUESTION = 3

    @classmethod
    def choices(cls):
        return (
            (cls.FEEDBACK, cls.type_to_name(cls.FEEDBACK)),
            (cls.CALLBACK, cls.type_to_name(cls.CALLBACK)),
            (cls.VISIT, cls.type_to_name(cls.VISIT)),
            (cls.QUESTION, cls.type_to_name(cls.QUESTION))
        )

    @classmethod
    def type_to_name(cls, email_type):
        if email_type == cls.FEEDBACK:
            return u'Форма обратной связи'
        elif email_type == cls.CALLBACK:
            return u'Обратный звонок'
        elif email_type == cls.VISIT:
            return u'Запись на приём'
        elif email_type == cls.QUESTION:
            return u'Задать вопрос'
        else:
            return u'Неизвестная форма'


class EmailRecipient(models.Model):
    email_type = models.SmallIntegerField(u'тип оповещения', choices=EmailTypesEnum.choices())
    recipient_email = models.EmailField(u'e-mail получателя')
    description = models.TextField(u'описание', blank=True, null=True)

    class Meta:
        verbose_name = u'получатель'
        verbose_name_plural = u'получатели уведомлений'

    def email_type_changelist(self):
        return EmailTypesEnum.type_to_name(self.email_type)
    email_type_changelist.short_description = u'Тип оповещения'

    def __unicode__(self):
        return self.recipient_email


class CallbackDeltaEnum(object):
    TIMES = [0, 300, 600, 900, 1800, 3600]

    @classmethod
    def choices(cls):
        return [[item, cls.time_to_text(item)] for item in cls.TIMES]

    @classmethod
    def time_to_text(cls, callback_time):
        if callback_time == 0:
            return u'сейчас'
        else:
            return u'через %d минут' % (callback_time/60,)


class Callback(models.Model):
    name = models.CharField(u'имя', max_length=255, blank=True, null=True)
    phone = models.CharField(u'телефонный номер', max_length=255)
    callback_delta = models.IntegerField(u'перезвонить', choices=CallbackDeltaEnum.choices(), default=0, blank=True, null=True)
    callback_time = models.DateTimeField(u'время звонка', blank=True, null=True)
    created_at = models.DateTimeField(u'создано', default=timezone.now)
    processed_at = models.DateTimeField(u'обработано', blank=True, null=True)

    class Meta:
        verbose_name = u'обратный звонок'
        verbose_name_plural = u'обратный звонок'

    def save(self, *args, **kwargs):
        self.callback_time = self.created_at+datetime.timedelta(seconds=self.callback_delta)
        super(Callback, self).save(*args, **kwargs)

    def get_callback_delta(self):
        return u'%s'%CallbackDeltaEnum.time_to_text(self.callback_delta)

    def get_callback_delta_changelist(self):
        return self.get_callback_delta()
    get_callback_delta_changelist.short_description = u'Перезвонить'

    def __unicode__(self):
        return self.phone

    @staticmethod
    def post_save(sender, instance, created, *args, **kwargs):
        if created:
            message_context = Context({
                'callback': instance,
                'site': Site.objects.get_current(get_request())
            })

            text_message_template = get_template('callback_email.txt')
            text_message = text_message_template.render(message_context)
            html_message_template = get_template('callback_email.html')
            html_message = html_message_template.render(message_context)

            send_mail(u'Перезвоните %s в %s (№ %d)' % (instance.get_callback_delta(), instance.callback_time.strftime('%Y.%m.%d %H:%M'), instance.id), text_message,
                settings.EMAIL_ADDRESS_FROM,
                EmailRecipient.objects.filter(email_type=EmailTypesEnum.CALLBACK).values_list('recipient_email', flat=True), html_message=html_message
            )

post_save.connect(Callback.post_save, sender=Callback)


class ProceduresEnum(object):
    NO_MATTER = 0
    FIRST = 1
    CONTINUE = 2

    @classmethod
    def choices(cls):
        return (
            (cls.NO_MATTER, cls.type_to_name(cls.NO_MATTER)),
            (cls.FIRST, cls.type_to_name(cls.FIRST)),
            (cls.CONTINUE, cls.type_to_name(cls.CONTINUE))
        )

    @classmethod
    def type_to_name(cls, procedure_type):
        if procedure_type == cls.NO_MATTER:
            return u'Не имеет значения'
        elif procedure_type == cls.FIRST:
            return u'Первичная консультация'
        elif procedure_type == cls.CONTINUE:
            return u'Повторный приём'
        else:
            return u'Неизвестно'


class VisitPurpose(models.Model):
    title = models.CharField(u'наименование', max_length=255, blank=True, null=True)

    class Meta:
        verbose_name = u'направление'
        verbose_name_plural = u'направления записи'

    def __unicode__(self):
        return self.title


class Visit(models.Model):
    name = models.CharField(u'имя', max_length=255, blank=True, null=True)
    phone = models.CharField(u'телефонный номер', max_length=255)
    email = models.EmailField(u'e-mail', blank=True, null=True)
    procedure = models.SmallIntegerField(u'вид процедуры', choices=ProceduresEnum.choices())
    purpose = models.ForeignKey(VisitPurpose, verbose_name='направление', blank=True, null=True)
    visit_date = models.DateField(u'дата приёма')
    visit_time = models.TimeField(u'время приёма')
    description = models.TextField(u'пожелания', blank=True, null=True)
    created_at = models.DateTimeField(u'создано', default=timezone.now)
    processed_at = models.DateTimeField(u'обработано', blank=True, null=True)

    class Meta:
        verbose_name = u'запись'
        verbose_name_plural = u'запись на приём'

    def __unicode__(self):
        return self.phone

    def get_procedure(self):
        return ProceduresEnum.type_to_name(self.procedure)

    def get_procedure_changelist(self):
        return self.get_procedure()
    get_procedure_changelist.short_description = u'Вид процедуры'

    @staticmethod
    def post_save(sender, instance, created, *args, **kwargs):
        if created:
            message_context = Context({
                'visit': instance,
                'site': Site.objects.get_current(get_request())
            })

            text_message_template = get_template('visit_email.txt')
            text_message = text_message_template.render(message_context)
            html_message_template = get_template('visit_email.html')
            html_message = html_message_template.render(message_context)

            send_mail(u'Online запись на %s в %s (№ %d)' % (instance.visit_date.strftime('%Y.%m.%d'), instance.visit_time.strftime('%H:%M'), instance.id), text_message,
                settings.EMAIL_ADDRESS_FROM,
                EmailRecipient.objects.filter(email_type=EmailTypesEnum.VISIT).values_list('recipient_email', flat=True), html_message=html_message
            )

post_save.connect(Visit.post_save, sender=Visit)


class Question(models.Model):
    name = models.CharField(u'имя', max_length=255, blank=True, null=True)
    question = models.TextField(u'вопрос')
    answer = models.TextField(u'ответ', blank=True, null=True)
    email = models.EmailField(u'e-mail')
    created_at = models.DateTimeField(u'создано', default=timezone.now)
    processed_at = models.DateTimeField(u'обработано', blank=True, null=True)
    is_published = models.BooleanField(u'опубликовано', default=False)

    class Meta:
        verbose_name = u'вопрос'
        verbose_name_plural = u'задать вопрос'

    def __unicode__(self):
        return self.question

    @staticmethod
    def post_save(sender, instance, created, *args, **kwargs):
        if created:
            message_context = Context({
                'question': instance,
                'site': Site.objects.get_current(get_request())
            })

            text_message_template = get_template('question_email.txt')
            text_message = text_message_template.render(message_context)
            html_message_template = get_template('question_email.html')
            html_message = html_message_template.render(message_context)

            send_mail(u'Вопрос требующий ответа (№ %d)' % instance.id, text_message,
                settings.EMAIL_ADDRESS_FROM,
                EmailRecipient.objects.filter(email_type=EmailTypesEnum.QUESTION).values_list('recipient_email', flat=True), html_message=html_message
            )

post_save.connect(Question.post_save, sender=Question)