from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from . import views

urlpatterns=[
    url('^$', views.index ,name="index"),
    url(r'^locations/$', views.sortby_locations, name='sortby_locations'),
    url(r'^search/', views.search_results, name='search_results'),
    url(r'^single/', views.single_image, name='single_image'),
   
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)