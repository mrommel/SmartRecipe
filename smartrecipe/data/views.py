from django.shortcuts import render

from django.http import HttpResponse
from django.http import Http404
import json

from .models import Recipe, RecipeTopic, RecipeCategory, Ingredient, RecipeIngredientRelation, RecipeBook


def index(request):
    # get all receipts
    recipe_list = Recipe.objects.all
    # get root topics
    topic_list = RecipeTopic.objects.filter(parentRecipeTopic=None)

    return render(request, 'data/index.html', {
        'recipe_list': recipe_list,
        'topic_list': topic_list,
    })


def recipes(request):
    # get all recipes
    recipe_list = Recipe.objects.all

    return render(request, 'data/recipes.html', {
        'recipe_list': recipe_list,
    })


def recipe(request, recipe_id):
    # get receipt (or fail)
    try:
        recipe_value = Recipe.objects.get(pk=recipe_id)
    except Recipe.DoesNotExist:
        raise Http404("Recipe does not exist")

    return render(request, 'data/recipe.html', {
        'recipe': recipe_value,
    })


def category(request, category_id):
    try:
        category_value = RecipeCategory.objects.get(pk=category_id)
    except RecipeCategory.DoesNotExist:
        raise Http404("Category does not exist")

    recipes_value = category_value.recipes()

    return render(request, 'data/category.html', {
        'recipes': recipes_value,
        'category': category_value,
    })


def categories(request):
    categories_value = RecipeCategory.objects.filter(parentRecipeCategory=None)

    return render(request, 'data/categories.html', {
        'categories': categories_value,
    })


def topic(request, topic_id):
    try:
        topic_value = RecipeTopic.objects.get(pk=topic_id)
    except RecipeTopic.DoesNotExist:
        raise Http404("Topic does not exist")

    return render(request, 'data/topic.html', {
        'topic': topic_value,
    })


def ingredient_search(request):
    recipe_list = Recipe.objects.all
    ingredient_list = Ingredient.objects.all()

    ingredient_name_list = []

    for ingredient in ingredient_list:
        ingredient_name = ingredient.name
        if ingredient_name is not None:
            ingredient_name = ingredient_name.replace(u'\xdf', '&szlig;')
        ingredient_name_list.append(str(ingredient_name))

    return render(request, 'data/ingredient_search.html', {
        'recipe_list': recipe_list,
        'ingredient_list': ingredient_list,
        'ingredient_name_list': ingredient_name_list,
    })


def recipes_by_ingredients(request):
    ingredient_names = request.GET.keys()[0].split(',')
    ingredients = []
    recipes = []

    for ingredient in ingredient_names:
        ingredient_objs = Ingredient.objects.filter(name__iexact=ingredient)
        if len(ingredient_objs):
            ingredients.append(ingredient_objs[0].id)

    for recipe in Recipe.objects.all():
        ranking = 0

        for receiptIngredientRelation in RecipeIngredientRelation.objects.filter(recipe=recipe):
            for ingredient_id in ingredients:
                if receiptIngredientRelation.ingredient.id == ingredient_id:
                    ranking = ranking + 1

        if ranking > 0:
            recipe_result = {'recipe_id': recipe.id, 'recipe_url': recipe.url(),
                             'recipe_image_url': recipe.image_url(), 'recipe_name': recipe.name,
                             'recipe_teaser': recipe.teaser, 'ranking': ranking}
            recipes.append(recipe_result)

    response_data = {'ingredient_names': ingredient_names, 'ingredients': ingredients, 'recipes': recipes}

    return HttpResponse(json.dumps(response_data), content_type="application/json")


def recipes_export(request, book_id):

    try:
        recipe_book = RecipeBook.objects.get(pk=book_id)
    except RecipeBook.DoesNotExist:
        raise Http404("RecipeBook does not exist")

    # get all recipes of book
    recipe_list = recipe_book.recipes()
    categories = RecipeCategory.objects.filter(parentRecipeCategory=None)
    ingredient_list = Ingredient.objects.all()

    return render(request, 'data/recipes_export.html', {
        'recipe_book': recipe_book,
        'recipe_list': recipe_list,
        'categories': categories,
        'ingredient_list': ingredient_list,
    })


def export(request, book_id):

    import os
    os.system(
        'prince --no-author-style --javascript -s http://127.0.0.1:8024/static/data/style_print.css http://127.0.0.1:8024/data/recipes_export/%s/export -o tmp.pdf' % book_id)

    image_data = open('tmp.pdf', "rb").read()
    return HttpResponse(image_data, content_type='application/pdf')
