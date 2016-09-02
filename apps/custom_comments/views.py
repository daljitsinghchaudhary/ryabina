# coding=utf-8
import json
import os
from PIL import Image
from django.conf import settings
from django.contrib.sites.models import get_current_site
from django.core.files.temp import NamedTemporaryFile
from django.http import HttpResponse, Http404
from django.views.generic import View, FormView
from annoying.functions import id_generator, create_dir, get_client_ip
from annoying.responses import JSONResponse
from apps.custom_comments.forms import ServiceCommentForm
from apps.custom_comments.models import CommentPhoto, CustomComment

if settings.DEBUG:
    import logging
    debug_logger = logging.getLogger('debug')


class CommentPhotoDelete(View):
    def post(self, request):
        result = {}
        file_id = request.POST.get('file_id')
        try:
            cp = CommentPhoto.objects.get(temp=file_id)
        except:
            result = { 'delete': False, 'filename': u'' , 'error_message' : u'Нет такого идентификатора %s' % file_id }
        else:
            if os.path.isfile(cp.photo.path):
                try:
                    os.unlink(cp.photo.path)
                except IOError:
                    result = { 'delete': False, 'filename': u'%s' % cp.photo.path, 'error_message' : u'Не могу удалить изображение' }
                else:
                    result = { 'delete': True, 'filename': u'', 'error_message' : u'' }
            else:
                result = { 'delete': False, 'filename': u'', 'error_message' : u'Нет такого файла' }
            cp.delete()
        return HttpResponse(json.dumps(result), content_type='text/html')


class CommentPhotoUpload(View):
    BUFFER_SIZE = 1024 * 512
    MAX_SIZE = 1024 * 1024 * 10
    IMAGE_PATH = os.path.join('images','comment')
    UPLOAD_DIR = os.path.join(settings.MEDIA_ROOT, IMAGE_PATH)
    IMAGE_SIZE = (160, 240)
    MAX_FILE_SIZE = 1024 * 512
    SUPPORTED_IMAGE_EXTS = ('.PNG', '.GIF', '.BMP', '.JPG', '.JPEG', '.PCX')

    def get_chunk(self, request):
        if 'qqfile' in request.FILES:
            chunk = request.FILES['qqfile'].file.read(self.BUFFER_SIZE)
        else:
            chunk = request.read(self.BUFFER_SIZE)
        return chunk

    def post(self, request):
        if 'qqfile' in request.GET:
            request_file_name = request.GET['qqfile']
            base, ext = os.path.splitext(request_file_name)
            if ext.upper() not in self.SUPPORTED_IMAGE_EXTS:
                result = { 'upload': False, 'filename': request_file_name, 'file_id': u'', 'error_message' : u'Тип файла не поддерживается' }
                return HttpResponse(json.dumps(result), content_type='text/html')

            create_dir(self.UPLOAD_DIR)

            destination = NamedTemporaryFile(delete=False, suffix=ext)
            temp_full_name = destination.name

            chunk = self.get_chunk(request)

            counted = 0
            while len(chunk) > 0:
                counted += len(chunk)
                if counted > self.MAX_FILE_SIZE:
                    destination.close()
                    os.remove(temp_full_name)
                    result = { 'upload': False, 'filename': request_file_name, 'file_id': u'', 'error_message' : u'Файл более 512КБ' }
                    return HttpResponse(json.dumps(result), content_type='text/html')

                destination.write(chunk)
                chunk = self.get_chunk(request)

            destination.close()
            file_name = '%s.jpeg' % id_generator()
            img = Image.open(temp_full_name)
            k = 1.0 * self.IMAGE_SIZE[1] / self.IMAGE_SIZE[0]
            h_new = int(k * img.size[0])
            if h_new != img.size[1]:
                if h_new < img.size[1]: # cut top and bottom
                    cut_top = int((img.size[1] - h_new) / 2.0)
                    cropped = img.crop((0, cut_top, img.size[0], cut_top + h_new))
                else:                   # cut left and right
                    w_new = int(img.size[1] / k)
                    cut_left = int((img.size[0] - w_new) / 2.0)
                    cropped = img.crop((cut_left, 0, cut_left + w_new, img.size[1]))
            else:
                cropped = img
            full_path = os.path.join(self.UPLOAD_DIR, file_name)
            finish_file = cropped.resize(self.IMAGE_SIZE, Image.ANTIALIAS)
            finish_file.convert('RGB').save(full_path, quality=100)

            os.unlink(temp_full_name)
            
            cp = CommentPhoto()
            cp.photo = '%s/%s' % (self.IMAGE_PATH, file_name)
            cp.save()
            
            result = { 'upload': True, 'filename': os.path.join(settings.MEDIA_URL, self.IMAGE_PATH, file_name), 'file_id': u'%s' % cp.temp, 'error_message' : u'' }
            # except Exception:
            #     result = { 'upload': False, 'filename': request_file_name, 'error_message' : u'Тип файла не поддерживается' }
            return HttpResponse(json.dumps(result), content_type='text/html')
        else:
            raise Http404()


class CommentView(FormView):
    form_class = ServiceCommentForm
    success_message = u'Спасибо! Благодаря вам, мы становимся лучше.'

    def get(self, request, *args, **kwargs):
        raise Http404()

    def get_comment_photo(self, temp):
        try:
            photo = CommentPhoto.objects.get(temp=temp)
        except CommentPhoto.DoesNotExist:
            return None
        else:
            return photo

    def form_valid(self, form):
        if settings.DEBUG:
            debug_logger.info(form.cleaned_data)

        comment = CustomComment()
        comment.rating = form.cleaned_data.get('rating', None)
        temp_photo = form.cleaned_data.get('photo', None)
        if temp_photo:
            comment.photo = self.get_comment_photo(temp_photo)
        comment.email = form.cleaned_data.get('email', None)
        comment.name = form.cleaned_data.get('name', None)
        comment.comment = form.cleaned_data.get('comment', None)
        comment.url = form.cleaned_data.get('url', None)
        content_type_id = form.cleaned_data.get('content_type', None)
        if content_type_id:
            comment.content_type_id = content_type_id
            if comment.content_type_id:
                comment_object = form.cleaned_data.get('object_pk', None)
                if comment_object:
                    comment.object_pk = comment_object.id
        comment.is_public = False
        comment.ip_address = get_client_ip(self.request)
        comment.site = get_current_site(self.request)
        comment.save()

        return JSONResponse({
            'success_message': self.success_message
        })

    def form_invalid(self, form):
        if settings.DEBUG:
            debug_logger.info(form.cleaned_data)
        raise Http404()