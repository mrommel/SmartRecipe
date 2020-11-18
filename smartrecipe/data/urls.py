#!/usr/bin/env python3

from django.conf.urls import *
from . import views

urlpatterns = [
    #url(r'^ingredient_search', views.ingredient_search, name='data.views.ingredient_search'),
    #url(r'^receipts_by_ingredients', views.receipts_by_ingredients, name='data.views.receipts_by_ingredients'),

    url(r'^$', views.index, name='index'),
    url(r'^recipes/', views.recipes, name='data.views.recipes'),
    url(r'^recipe/(?P<recipe_id>\d+)', views.recipe, name='data.views.recipe'),
    url(r'^categories/', views.categories, name='data.views.categories'),
    url(r'^category/(?P<category_id>\d+)', views.category, name='data.views.category'),
    url(r'^topic/(?P<topic_id>\d+)', views.topic, name='data.views.topic'),

    url(r'^recipes_export/(?P<book_id>\d+)', views.recipes_export, name='data.views.recipes_export'),
    url(r'^export/(?P<book_id>\d+)/recipes/', views.export, name='data.views.export'),
]