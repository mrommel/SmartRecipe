from django.db.migrations.serializer import BaseSerializer, SequenceSerializer, TypeSerializer
#from rest_framework.serializers import HyperlinkedModelSerializer

from .models import Recipe, IngredientType, Ingredient, RecipeCategory


class ReceiptIngredientRelationSerializer(BaseSerializer):

    def __init__(self, value):
        self.value = value

    def serialize(self):
        ingredients = []

        for ingredient_relation in self.value:
            ingredient = dict()
            ingredient['id'] = ingredient_relation.ingredient.id
            ingredient['quantity'] = ingredient_relation.amount
            ingredient['type'] = ingredient_relation.amount_type
            ingredients.append(ingredient)

        return ingredients


class ReceiptCategoriesRelationSerializer(BaseSerializer):

    def __init__(self, value):
        self.value = value

    def serialize(self):
        categories = []

        for category_relation in self.value:
            if not category_relation.recipeCategory.is_country:
                category = dict()
                category['id'] = category_relation.recipeCategory.id
                categories.append(category)

        return categories


class CountryCategorySerializer(BaseSerializer):

    def __init__(self, value):
        self.value = value

    def serialize(self):
        name = ''
        flag = ''
        has_country = False

        for item in self.value:
            name = item.name
            flag = '/media/%s' % item.image.name
            has_country = True

        if has_country:
            return {
                'country': {
                    'name': name,
                    'flag': flag
                }
            }
        else:
            return {
                'country': {
                }
            }


class ReceiptStepSerializer(BaseSerializer):

    def __init__(self, value):
        self.value = value

    def serialize(self):
        return {
            'step': {
                'index': self.value.index,
                'text': self.value.text
            }
        }

#
# class ReceiptStepSerializer(SequenceSerializer):
#
#     def __init__(self, value):
#         self.value = value
#
#     #child = ReceiptStepSerializer()
#
#
# class ReceiptSerializer(HyperlinkedModelSerializer):
#
#     class Meta:
#         model = Receipt
#         fields = (
#             'id', 'name', 'teaser', 'description', 'image_url', 'time', 'calories', 'portions', 'steps', 'countries',
#             'ingredients', 'categories',)
#
#
# class IngredientTypeSerializer(HyperlinkedModelSerializer):
#
#     class Meta:
#         model = IngredientType
#         fields = ('name',)
#
#
# class IngredientSerializer(HyperlinkedModelSerializer):
#
#     class Meta:
#         model = Ingredient
#         fields = ('id', 'name', 'type', 'image_url',)
#
#
# class CategorySerializer(HyperlinkedModelSerializer):
#
#     def __init__(self, value):
#         self.value = value
#
#     class Meta:
#         model = ReceiptCategory
#         fields = ('id', 'path', 'name', 'parent_id', 'number_of_receipts', 'image_url',)
