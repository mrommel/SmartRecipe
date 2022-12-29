from django.conf.urls import *
from django.contrib import admin
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path
from django.views.generic import RedirectView
from django.conf.urls.static import static

# from rest_framework import routers

urlpatterns = [
    path(r'', RedirectView.as_view(url='/data/index')),
    path(r'data/', include('data.urls')),
    path('admin/', admin.site.urls),
    path(r'i18n/', include('django.conf.urls.i18n')),
    path(r'favicon\.ico', RedirectView.as_view(url=settings.MEDIA_URL + 'images/favicon.ico')),

    # api
    # url(r'^', include(router.urls)),
    # url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
