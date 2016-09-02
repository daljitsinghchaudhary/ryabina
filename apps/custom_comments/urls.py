# coding=utf-8
from django.conf.urls import url
from apps.custom_comments.views import CommentPhotoUpload, CommentPhotoDelete, CommentView

urlpatterns =[
    url(r'^upload_photo/$', CommentPhotoUpload.as_view(), name='upload_photo'),
    url(r'^delete_photo/', CommentPhotoDelete.as_view(), name='delete_photo'),
    url(r'^add/$', CommentView.as_view(), name='add_comment'),
]