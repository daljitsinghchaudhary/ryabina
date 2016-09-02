# coding=utf-8
from django.http import Http404
from django.views.generic import FormView
from annoying.responses import JSONResponse
from apps.questions.forms import CallbackForm, QuestionForm, VisitForm


class CallbackView(FormView):
    form_class = CallbackForm
    success_message = u'Спасибо за обращение. Заявка отправлена. Мы свяжемся с вами в указанное время.'

    def get(self, request, *args, **kwargs):
        raise Http404()

    def form_valid(self, form):
        form.save()
        return JSONResponse({
            'success_message': self.success_message
        })


class QuestionView(CallbackView):
    form_class = QuestionForm
    success_message = u'Спасибо за обращение. Наши специалисты ответят вам в ближайшее время.'


class VisitView(CallbackView):
    form_class = VisitForm
    success_message = u'Спасибо за обращение. Мы свяжемся с вами в ближайшее время чтобы уточнить детали.'