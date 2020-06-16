from django.conf.urls import *
from django.contrib import admin
from django.conf import settings
from django.urls import path
from django.views.generic import RedirectView

from rest_framework import routers

#from smartrecipe.data import views
#
#router = routers.DefaultRouter()
#router.register(r'recipes', views.RecipesViewSet)
#router.register(r'ingredients', views.IntegrientsViewSet)
#router.register(r'categories', views.CategorysViewSet)

urlpatterns = [
    url(r'^$', RedirectView.as_view(url='/data/index')),
    url(r'^data/', include('data.urls')),
    path('admin/', admin.site.urls),
    url(r'^i18n/', include('django.conf.urls.i18n')),
    url(r'^favicon\.ico$', RedirectView.as_view(url=settings.MEDIA_URL + 'images/favicon.ico')),

    # api
    #url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
