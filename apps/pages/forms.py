# -*- coding: utf-8 -*-
from captcha.fields import CaptchaField, CaptchaTextInput
from django import forms
from django.conf import settings
from annoying.fields import EmailField


class FeedbackForm(forms.Form):
    name = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'placeholder': u'Имя'}), label=u'Представьтесь:')
    email = EmailField(max_length=50, widget=forms.EmailInput(attrs={'placeholder': u'example@mail.ru'}), label=u'E-mail:')
    phone = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'placeholder': u'+7 (', 'class': u'form-control masked_input_mobile'}), required=False, label=u'Телефон:')
    text = forms.CharField(max_length=2000, widget=forms.Textarea(attrs={'placeholder': 'Сообщение', 'rows':5}), label=u'Сообщение:')
    attachment = forms.FileField(label=u'Документ:', required=False)
    captcha = CaptchaField(widget=CaptchaTextInput(attrs={'placeholder': u'Введите код', 'class': u'form-control captcha-inline'}), label=u'Код проверки:')

    def clean_attachment(self):
        if self.cleaned_data['attachment']:
            if self.cleaned_data['attachment'].size > settings.MAX_ATTACH_FEEDBACK_FILE_SIZE:
                raise forms.ValidationError(u'Превышен размер файла')
        return self.cleaned_data['attachment']


class SubscriptionForm(forms.Form):
    name = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'placeholder': u'Имя'}), label=u'Представьтесь')
    email = EmailField(max_length=50, widget=forms.EmailInput(attrs={'placeholder': u'example@mail.ru'}), label=u'E-mail')
    # course = forms.CharField(widget=forms.ChoiceField(attrs={'placeholder': u'Направление'}), label=u'Направление:')
    captcha = CaptchaField(widget=CaptchaTextInput(attrs={'placeholder': u'Введите код', 'class': u'form-control captcha-inline'}), label=u'Код проверки')

    # def __init__(self, *args, **kwargs):
    #     super(SubscriptionForm, self).__init__(*args, **kwargs)
    #     self.fields['course'].choices = [[None,'Не имеет значение']]+list(VisitPurpose.objects.values_list('id','title'))
    #     self.fields['course'].initial = None