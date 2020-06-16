from django.shortcuts import render

from django.http import HttpResponse
from django.http import Http404
import json

from rest_framework.viewsets import ModelViewSet

from .serializers import ReceiptSerializer, IngredientSerializer, CategorySerializer

from .models import Receipt, Ingredient, ReceiptIngredientRelation, ReceiptTopic, ReceiptCategory


def index(request):
    # get all receipts
    receipt_list = Receipt.objects.all
    # get root topics
    topic_list = ReceiptTopic.objects.filter(parentReceiptTopic=None)

    return render(request, 'data/index.html', {
        'receipt_list': receipt_list,
        'topic_list': topic_list,
    })


def receipts(request):
    # get all receipts
    receipt_list = Receipt.objects.all

    return render(request, 'data/receipts.html', {
        'receipt_list': receipt_list,
    })


def receipt(request, receipt_id):
    # get receipt (or fail)
    try:
        receipt_value = Receipt.objects.get(pk=receipt_id)
    except Receipt.DoesNotExist:
        raise Http404("Receipt does not exist")

    return render(request, 'data/receipt.html', {
        'receipt': receipt_value,
    })


def category(request, category_id):
    try:
        category_value = ReceiptCategory.objects.get(pk=category_id)
    except ReceiptCategory.DoesNotExist:
        raise Http404("Category does not exist")

    receipts_value = category_value.receipts()

    return render(request, 'data/category.html', {
        'receipts': receipts_value,
        'category': category_value,
    })


def categories(request):
    categories_value = ReceiptCategory.objects.filter(parentReceiptCategory=None)

    return render(request, 'data/categories.html', {
        'categories': categories_value,
    })


def topic(request, topic_id):
    try:
        topic_value = ReceiptTopic.objects.get(pk=topic_id)
    except ReceiptTopic.DoesNotExist:
        raise Http404("Topic does not exist")

    return render(request, 'data/topic.html', {
        'topic': topic_value,
    })


def ingredient_search(request):

    receipt_list = Receipt.objects.all
    ingredient_list = Ingredient.objects.all()

    ingredient_name_list = []

    for ingredient in ingredient_list:
        ingredient_name = ingredient.name
        ingredient_name = ingredient_name.replace(u'\xdf', '&szlig;')
        ingredient_name_list.append(str(ingredient_name))

    return render(request, 'data/ingredient_search.html', {
        'receipt_list': receipt_list,
        'ingredient_list': ingredient_list,
        'ingredient_name_list': ingredient_name_list,
    })


def receipts_by_ingredients(request):
    ingredient_names = request.GET.keys()[0].split(',')
    ingredients = []
    receipts = []

    for ingredient in ingredient_names:
        ingredient_objs = Ingredient.objects.filter(name__iexact=ingredient)
        if len(ingredient_objs):
            ingredients.append(ingredient_objs[0].id)

    for receipt in Receipt.objects.all():
        ranking = 0

        for receiptIngredientRelation in ReceiptIngredientRelation.objects.filter(receipt=receipt):
            for ingredient_id in ingredients:
                if receiptIngredientRelation.ingredient.id == ingredient_id:
                    ranking = ranking + 1

        if ranking > 0:
            receipt_result = {'receipt_id': receipt.id, 'receipt_url': receipt.url(),
                              'receipt_image_url': receipt.image_url(), 'receipt_name': receipt.name,
                              'receipt_teaser': receipt.teaser, 'ranking': ranking}
            receipts.append(receipt_result)

    response_data = {'ingredient_names': ingredient_names, 'ingredients': ingredients, 'receipts': receipts}

    return HttpResponse(json.dumps(response_data), content_type="application/json")


def receipts_export(request):
    # get all receipts
    receipt_list = Receipt.objects.all
    categories = ReceiptCategory.objects.filter(parentReceiptCategory=None)
    ingredient_list = Ingredient.objects.all()

    return render(request, 'data/receipts_export.html', {
        'receipt_list': receipt_list,
        'categories': categories,
        'ingredient_list': ingredient_list,
    })


def export(request):
    import os
    os.system(
        'prince --no-author-style --javascript -s http://127.0.0.1:8000/static/data/style_print.css http://127.0.0.1:8000/data/receipts_export/export -o tmp.pdf')

    image_data = open('tmp.pdf', "rb").read()
    return HttpResponse(image_data, content_type='application/pdf')


class RecipesViewSet(ModelViewSet):
    """
    API endpoint that allows recipes to be viewed or edited.
    """
    queryset = Receipt.objects.all()
    serializer_class = ReceiptSerializer


class IntegrientsViewSet(ModelViewSet):
    """
    API endpoint that allows integrient to be viewed or edited.
    """
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer


class CategorysViewSet(ModelViewSet):
    """
    API endpoint that allows integrient to be viewed or edited.
    """
    queryset = ReceiptCategory.objects.filter(is_country=False)
    serializer_class = CategorySerializer
