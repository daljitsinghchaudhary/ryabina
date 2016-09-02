# -*- coding: utf-8 -*-
from captcha.fields import CaptchaField, CaptchaTextInput
from django import forms
from django.utils import timezone
from annoying.fields import EmailField
from apps.questions.models import Callback, CallbackDeltaEnum, Question, Visit, ProceduresEnum, VisitPurpose


class QuestionForm(forms.ModelForm):
    name = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'placeholder': u'Имя'}), label=u'Представьтесь')
    captcha = CaptchaField(widget=CaptchaTextInput(attrs={'placeholder': u'Введите код', 'class': u'form-control captcha-inline'}), label=u'Код проверки')
    email = EmailField(max_length=50, widget=forms.EmailInput(attrs={'placeholder': u'example@mail.ru'}), label=u'E-mail')
    question = forms.CharField(max_length=2000, widget=forms.Textarea(attrs={'placeholder': 'Вопрос', 'rows':5}), label=u'Вопрос')

    class Meta:
        model = Question
        fields = ['name', 'email', 'question']


class VisitForm(forms.ModelForm):
    name = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'placeholder': u'Имя'}), label=u'Представьтесь')
    phone = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'placeholder': u'+7 (', 'class': u'form-control masked_input_mobile'}), required=False, label=u'Телефон')
    email = EmailField(max_length=50, widget=forms.EmailInput(attrs={'placeholder': u'example@mail.ru'}), label=u'E-mail')
    description = forms.CharField(max_length=2000, widget=forms.Textarea(attrs={'placeholder': 'Пожелания', 'rows':5}), label=u'Пожелания')
    captcha = CaptchaField(widget=CaptchaTextInput(attrs={'placeholder': u'Введите код', 'class': u'form-control captcha-inline'}), label=u'Код проверки')

    def __init__(self, *args, **kwargs):
        super(VisitForm, self).__init__(*args, **kwargs)
        self.fields['procedure'].choices = ProceduresEnum.choices()
        self.fields['procedure'].initial = 0
        self.fields['purpose'].choices = [[None,'Не имеет значение']]+list(VisitPurpose.objects.values_list('id','title'))
        self.fields['purpose'].initial = None
        self.short_fields = ['phone', 'purpose', 'email', 'procedure', 'visit_date', 'visit_time']
        if hasattr(self.instance, 'visit_date') and not self.instance.visit_date:
            self.fields['visit_date'].initial = timezone.localtime(timezone.now()).strftime('%Y-%m-%d')
        if hasattr(self.instance, 'visit_time') and not self.instance.visit_time:
            self.fields['visit_time'].initial = timezone.localtime(timezone.now()).strftime('%H:%M')

    class Meta:
        model = Visit
        fields = ['name', 'phone', 'email', 'purpose', 'procedure', 'visit_date', 'visit_time', 'description']


class CallbackForm(forms.ModelForm):
    name = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'placeholder': u'Имя'}), label=u'Представьтесь')
    phone = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'placeholder': u'+7 (', 'class': u'form-control masked_input_mobile'}), required=False, label=u'Телефон')
    captcha = CaptchaField(widget=CaptchaTextInput(attrs={'placeholder': u'Введите код', 'class': u'form-control captcha-inline'}), label=u'Код проверки')

    def __init__(self, *args, **kwargs):
        super(CallbackForm, self).__init__(*args, **kwargs)
        self.fields['callback_delta'].choices = CallbackDeltaEnum.choices()
        self.fields['callback_delta'].initial = 0

    class Meta:
        model = Callback
        fields = ['name', 'phone', 'callback_delta']