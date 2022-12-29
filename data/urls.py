#!/usr/bin/env python3

from django.urls import path

from . import views

urlpatterns = [
    #url(r'^ingredient_search', views.ingredient_search, name='data.views.ingredient_search'),
    #url(r'^receipts_by_ingredients', views.receipts_by_ingredients, name='data.views.receipts_by_ingredients'),

    path(r'', views.index, name='index'),
    path(r'recipes/', views.recipes, name='data.views.recipes'),
    path(r'recipe/<int:recipe_id>', views.recipe, name='data.views.recipe'),
    path(r'categories/', views.categories, name='data.views.categories'),
    path(r'category/<int:category_id>', views.category, name='data.views.category'),
    path(r'topic/<int:topic_id>', views.topic, name='data.views.topic'),

    path(r'recipes_export/<int:book_id>', views.recipes_export, name='data.views.recipes_export'),
    path(r'export/<int:book_id>/recipes/', views.export, name='data.views.export'),
]