# coding=utf-8
import os
from django.conf import settings
from django.contrib import messages
from django.contrib.contenttypes.models import ContentType
from django.contrib.sites.models import Site, get_current_site
from django.contrib.staticfiles.views import serve
from django.core.mail import EmailMultiAlternatives
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, Http404, HttpResponsePermanentRedirect, HttpResponse
from django.shortcuts import get_object_or_404
from django.template import Context, loader, RequestContext
from django.template.loader import get_template
from django.utils.safestring import mark_safe
from django.views.decorators.csrf import csrf_protect
from django.views.generic import TemplateView, View, FormView
from django.utils import timezone
from newsletter.models import Subscription, Newsletter
from annoying.functions import get_client_ip
from apps.custom_comments import CustomComment
from apps.custom_comments.forms import ServiceCommentForm
from apps.discounts.models import Discount
from apps.newsboard.models import News
from apps.pages.forms import FeedbackForm, SubscriptionForm
from apps.pages.models import FlatPage
from apps.questions.models import EmailRecipient, EmailTypesEnum
from apps.services.models import ServiceCourse, ServiceCategory
from apps.slideshow.models import RotatingImage, ParallaxImage, ContactsImage, ContactsImagesType


class MainView(TemplateView):
    template_name = 'main.html'

    def get_context_data(self, **kwargs):
        context = super(MainView, self).get_context_data(**kwargs)
        now = timezone.now()
        context.update({
            'slideshow': RotatingImage.objects.all(),
            'courses': ServiceCourse.objects.filter(on_main_page=True),
            'parallax': ParallaxImage.objects.all().order_by('?').first(),
            'contacts_image': ContactsImage.objects.all().order_by('?').first(),
            'discounts': Discount.objects.filter(is_published=True, created_at__lt=now).exclude(close_at__lte=now),
            'newsboard': News.objects.filter(on_main_page=True, is_published=True).exclude(close_at__lte=now)[:9],
        })
        return context


class ServicesView(FormView):
    form_class = SubscriptionForm
    template_name = 'services.html'
    success_url = None
    category_id = None

    def get_success_url(self):
        return u'%s#discounts' % reverse('pages:services')

    def get(self, request, *args, **kwargs):
        self.category_id = kwargs.get('category_id')
        if self.category_id is not None:
            self.category_id = int(self.category_id)
            if not ServiceCategory.objects.filter(id=self.category_id).count():
                raise Http404()
        return super(ServicesView, self).get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(ServicesView, self).get_context_data(**kwargs)
        now = timezone.now()
        content_type = ContentType.objects.get_for_model(ServiceCategory)
        context.update({
            'category_id': self.category_id,
            'parallax': ParallaxImage.objects.all().order_by('?').first(),
            'slideshow_image': RotatingImage.objects.all().order_by('?').first(),
            'discounts': Discount.objects.filter(is_published=True, created_at__lt=now).exclude(close_at__lte=now),
            'categories': ServiceCategory.objects.all(),
            'comment_form': ServiceCommentForm(),
            'comments': CustomComment.objects.filter(is_public=True, content_type=content_type)
        })
        return context

    def get_services_newsletter(self):
        try:
            newsletter = Newsletter.objects.get(title=u'Новая акция')
        except Newsletter.DoesNotExist:
            newsletter = Newsletter()
            newsletter.title = u'Новая акция'
            newsletter.email = settings.DEFAULT_NEWSLETTER_EMAIL
            newsletter.sender = settings.DEFAULT_NEWSLETTER_SENDER
            newsletter.send_html = True
            newsletter.visible = True
            newsletter.slug=u'novaya-akciya'
            newsletter.save()
            newsletter.site.add(*Site.objects.all())
        return newsletter

    def form_valid(self, form):
        newsletter = self.get_services_newsletter()
        email = form.cleaned_data['email']
        try:
            subscription = Subscription.objects.get(email_field=email, newsletter=newsletter)
        except Subscription.DoesNotExist:
            subscription = Subscription()
            subscription.email = form.cleaned_data['email']
            subscription.name = form.cleaned_data['name']
            subscription.newsletter = self.get_services_newsletter()
            subscription.save()
            subscription.send_activation_email(action='subscribe')
            messages.success(self.request, u'Вы подписались на уведомления о новых акциях стоматологического центра "Рябина"!')
        else:
            if subscription.subscribed:
                messages.success(self.request, u'Вы уже подписаны на уведомления о новых акциях стоматологического центра "Рябина"!')
            else:
                subscription.send_activation_email(action='subscribe')
                messages.success(self.request, u'Мы выслали вам письмо активации на уведомления о новых акциях стоматологического центра "Рябина"!')
        return HttpResponseRedirect(self.get_success_url())


class ContactsView(FormView):
    form_class = FeedbackForm
    template_name = 'contacts.html'
    success_url = None

    def get_success_url(self):
        return reverse('pages:contacts')

    def get_context_data(self, **kwargs):
        context = super(ContactsView, self).get_context_data(**kwargs)
        context.update({
            'contacts_images': ContactsImage.objects.all(),
            'contacts_images_types': ContactsImagesType.objects.all(),
        })
        return context

    def form_valid(self, form):
        user_email = form.cleaned_data['email']
        text = form.cleaned_data['text']
        name = form.cleaned_data['name']
        phone = form.cleaned_data['phone']

        browser_info = u'IP адрес: %s, браузер: %s' % (get_client_ip(self.request), self.request.META['HTTP_USER_AGENT'])

        message_context = Context({
            'phone': phone,
            'name': name,
            'text': text,
            'user_email': user_email,
            'browser_info': browser_info
        })

        message_text_template = get_template('feedback_email.txt')
        message_text = message_text_template.render(message_context)
        message_html_template = get_template('feedback_email.html')
        message_html = message_html_template.render(message_context)

        msg = EmailMultiAlternatives(u'Сообщение обратной связи', message_text, settings.EMAIL_ADDRESS_FROM,
        EmailRecipient.objects.filter(email_type=EmailTypesEnum.FEEDBACK).values_list('recipient_email', flat=True),)
        msg.attach_alternative(message_html, "text/html")

        if form.cleaned_data['attachment']:
            attachment = self.request.FILES['attachment']
            msg.attach(attachment.name, attachment.file.read(), attachment.content_type)

        msg.send()
        messages.success(self.request, u'Сообщение успешно отправлено в стоматологический центр Рябина, в ближайшее время с вами свяжется администратор!')
        return HttpResponseRedirect(self.get_success_url())


class FlatpageView(View):
    DEFAULT_TEMPLATE = 'flatpages/default.html'

    def get(self, request, url):
        return self.flatpage(request, url)

    def flatpage(self, request, url):
        if not url.startswith('/'):
            url = '/' + url
        site_id = get_current_site(request).id
        try:
            f = get_object_or_404(FlatPage, url__exact=url, sites__id__exact=site_id)
        except Http404:
            if not url.endswith('/') and settings.APPEND_SLASH:
                url += '/'
                f = get_object_or_404(FlatPage, url__exact=url, sites__id__exact=site_id)
                return HttpResponsePermanentRedirect('%s/' % request.path)
            else:
                raise
        if f.unpublish:
            raise Http404
        return self.render_flatpage(request, f)

    @csrf_protect
    def render_flatpage(self, request, f):
        if f.registration_required and not request.user.is_authenticated():
            from django.contrib.auth.views import redirect_to_login
            return redirect_to_login(request.path)
        if f.template_name:
            t = loader.select_template((f.template_name, self.DEFAULT_TEMPLATE))
        else:
            t = loader.get_template(self.DEFAULT_TEMPLATE)

        f.title = mark_safe(f.title)
        f.content = mark_safe(f.content)

        c = RequestContext(request, {
            'flatpage': f,
        })
        response = HttpResponse(t.render(c))
        return response


class FaviconView(View):
    def get(self, request):
        return serve(request, os.path.join('img', 'favicon.ico'))
