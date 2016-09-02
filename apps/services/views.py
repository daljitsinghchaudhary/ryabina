# coding=utf-8
from StringIO import StringIO
import PIL
from django.conf import settings
from django.contrib.sites.shortcuts import get_current_site
from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseServerError, HttpResponseBadRequest
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.template.loader import get_template
from django.views.generic import View
import qrcode
from xhtml2pdf import pisa
from django.utils import timezone
from apps.discounts.models import Discount
from apps.services.models import Service, ServiceCourse


class PriceView(View):
    template_name = 'price_pdf.html'
    def get(self, request):
        now = timezone.now()
        context = {
            'courses': ServiceCourse.objects.all(),
            'services': Service.get_annotated_list(),
            'discounts': Discount.objects.filter(is_published=True, created_at__lt=now).exclude(close_at__lte=now),
            'qr_data': 'http://%s%s' % (get_current_site(request), reverse('pages:services')),
            'qr_host': 'www.ryabinaclinic.ru'
        }

        template = get_template(self.template_name)
        # return render_to_response(self.template_name, context, context_instance=RequestContext(request))

        result = StringIO()
        pdf = pisa.pisaDocument(StringIO(template.render(context).encode("UTF-8")), result)
        if not pdf.err:
            response = HttpResponse(result.getvalue(), content_type='application/pdf')
            response['Content-Disposition'] = 'attachment; filename=ryabina_price_%s.pdf' % timezone.now().strftime('_%Y_%m_%d__%H_%M')
            return response
        else:
            return HttpResponseServerError()


class ViewQRCode(View):
    def get(self, request):
        if 'qr_pass_phrase' in request.GET and len(request.GET['qr_pass_phrase']) and request.GET['qr_pass_phrase'] == settings.QR_PASS_PHRASE:
            if 'data' in request.GET and len(request.GET['data']):
                info = request.GET['info']
            else:
                info = u'(Ryabina, %s) http://www.ryabina-stom.ru' % timezone.now().strftime('%Y')

            qr = qrcode.QRCode(
                version=1,
                error_correction=qrcode.constants.ERROR_CORRECT_L,
                box_size=10,
                border=0,
            )
            qr.add_data(info)
            qr.make(fit=True)

            img = qr.make_image()

            try:
                size = int(request.GET['size']) if 'size' in request.GET and len(request.GET['size']) else 300
            except ValueError:
                size = 300

            img_ratio = size/float(img._img.size[0])
            img = img._img.resize([int(img_ratio * s) for s in img._img.size], PIL.Image.ANTIALIAS)

            response = HttpResponse(content_type='image/png')
            img.save(response,'png')

            return response
        else:
            return HttpResponseBadRequest()