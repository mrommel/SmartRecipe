#!/usr/bin/env python3

from django.conf.urls import *
from . import views
from django.views.generic import RedirectView

urlpatterns = [
    #url(r'^$', RedirectView.as_view(url='/index/')),
    #url(r'^index/', views.index, name='data.views.index'),
    #url(r'^receipts/', views.receipts, name='data.views.receipts'),
    #url(r'^receipts_export/', views.receipts_export, name='data.views.receipts_export'),
    #url(r'^receipt/(?P<receipt_id>\d+)', views.receipt, name='data.views.receipt'),
    #url(r'^category/(?P<category_id>\d+)', views.category, name='data.views.category'),
    #url(r'^categories/', views.categories, name='data.views.categories'),
    #url(r'^topic/(?P<topic_id>\d+)', views.topic, name='data.views.topic'),
    #url(r'^ingredient_search', views.ingredient_search, name='data.views.ingredient_search'),
    #url(r'^receipts_by_ingredients', views.receipts_by_ingredients, name='data.views.receipts_by_ingredients'),
    #url(r'^export/receipts/', views.export, name='data.views.export'),

    url('', views.index, name='index')
]