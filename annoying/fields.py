# -*- coding: utf-8 -*-
from django.core import validators
from django.forms import CharField, EmailInput


class EmailField(CharField):
    widget = EmailInput
    default_validators = [validators.EmailValidator(u'Введите правильный адрес электронной почты')]

    def clean(self, value):
        value = self.to_python(value).strip()
        return super(EmailField, self).clean(value)