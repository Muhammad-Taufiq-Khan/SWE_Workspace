from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from sentiment import views


urlpatterns = [
    path('', views.my_form),

]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)








# from django.shortcuts import render
# from django.http import HttpResponse
# from django.urls import path
# from sentiment import views
#
# urlpatterns = [
#     path('', views.homepage),
#     path(r'form', views.my_form, name='form')
#
#
# ]



































